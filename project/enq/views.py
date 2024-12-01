from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Format, Question, Enquete, Item, Answer
from .forms import QuestionForm

def index(request):
  return render(request, 'enq/index.html')

def enq_list(request):
  if request.method == 'POST':
    enq_title = request.POST.get('title') #enq_listからとってくる
    Enquete.objects.create(title=enq_title)
    enq = Enquete.objects.order_by('enq_id').last()
    enq_id = enq.enq_id #enq_id取得

    redirect_url = reverse('enq:create', args=[enq_id])
    return redirect(redirect_url)

  enquetes = Enquete.objects.order_by('enq_id').all()
  print(enquetes, '-------------enq_list get----------------')
  
  params = {
    'enquetes':enquetes,
  }
  return render(request, 'enq/enq_list.html', params)


def create(request, enq_id):
  if request.method == 'POST':
    print('---------------------------------createのPOST-aaaa-----------------------------------------')

    posted_question = request.POST.get('question')
    posted_format = int(request.POST.get('format'))
    print('posted_format', posted_format)
    order_no = request.POST.get('order_no')


    # DBに登録する処理
    question = Question.objects.create(question=posted_question, format_id=posted_format, order_no=order_no, enq_id=enq_id)
    # question = Question.objects.create(question=posted_question, format_id=Format(fomat_id=posted_format), order_no=order_no, enq_id=enq_id)
    
    if posted_format == 1:
      for i in range(1, 6):
        item = request.POST.get(f'item{i}')
        Item.objects.create(question=question, item=item)
    elif posted_format == 2:
      for i in range(1, 8):
        item = request.POST.get(f'item{i}')
        Item.objects.create(question=question, item=item)

    
    redirect_url = reverse('enq:create', args=[enq_id])
    return redirect(redirect_url)

  # initial_data = {
  #   'enq_id':enq_id,
  # }
  # form = QuestionForm(initial=initial_data)

  #dbから取得
  question = Question.objects.filter(enq_id=enq_id).order_by('order_no')
  enquete = Enquete.objects.filter(enq_id=enq_id).first()

  #paramsで辞書渡す
  params = {
    'question':question,
    'enq_id':enq_id,
    'enquete':enquete,
  }
  
  return render(request, 'enq/create.html', params)


@csrf_exempt
def answer(request, enq_id):
  if request.method=='POST':
    cnt = request.POST.get('cnt')
    for i in cnt:
      ans = request.POST.get(f'ans{i}')
      question_id = request.POST.get(f'question_id{i}')
      Question.objects.update_or_create(id=question_id, defaults={'answer':ans})
    # print(radio1Ans)

    # Answer.objects.create(answer=radio1Ans)
    # Question.objects.update_or_create(enq_id=enq_id, defaults={'answer':Answer(answer=radio1Ans)})

    redirect_url = reverse('enq:end', args=[enq_id])
    return redirect(redirect_url) 

  print('----------------answer GET------------------------')
  #dbから取得
  question = Question.objects.filter(enq_id=enq_id).order_by('order_no')
  print('question[0].__dict__', question[0].__dict__)
  print('question[0].items.all()', question[0].items.all())
  print('question[0].items.all()[0]', question[0].items.all()[0])
  items = Item.objects.order_by('item_id').all()
  item = question[0].items.all()

  #paramsで辞書渡す
  params = {
    'question':question,
    'item':item,
    'items':items,
    'enq_id':enq_id,
  }
  
  return render(request, 'enq/answer.html', params)

def end(request):
  return render(request, 'enq/end.html')

def check(request, enq_id):


  #dbから取得
  question = Question.objects.filter(enq_id=enq_id).order_by('order_no')
  
  return render(request, 'enq/check.html')
