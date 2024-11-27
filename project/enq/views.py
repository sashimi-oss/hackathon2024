from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def index(request):
  return render(request, 'enq/index.html')

def create(request):
  if request.method == 'POST':
    print('---------------------------------createのPOST------------------------------------------')
    return redirect('enq:index')
  

  return render(request, 'enq/create.html')

def check(request):
  return render(request, 'enq/check.html')
