from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def index(request):
  return render(request, 'enq/index.html')

def create(request):
  if request.method == 'POST':
    print('---------------------------------createのPOST------------------------------------------')
    # DBに登録する処理
    

    return redirect('enq:create')
  
  return render(request, 'enq/create.html')

def check(request):
  return render(request, 'enq/check.html')
