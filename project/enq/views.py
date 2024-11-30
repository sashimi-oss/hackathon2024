from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Format, Question, Enquete
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
    posted_format = request.POST.get('format')
    order_no = request.POST.get('order_no')
    if posted_format:
      posted_format = int(posted_format)
    # print(type(posted_format))
    # print(posted_format)
    # test = request.POST.get('test')
    # print('text->',posted_question)
    # print('test',test)
    

    # DBに登録する処理
    Question.objects.create(question=posted_question, format_id=Format(format_id = posted_format), order_no=order_no, enq_id_id=enq_id)
    
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

def answer(request, enq_id):

  #dbから取得
  question = Question.objects.filter(enq_id=enq_id).order_by('order_no')

  #paramsで辞書渡す
  params = {
    'question':question,
    'enq_id':enq_id,
  }
  
  return render(request, 'enq/answer.html', params)
