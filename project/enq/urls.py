from django.urls import path
from . import views

app_name = 'enq'
urlpatterns = [
  path('', views.index, name='index'),
  path('enq_list/', views.enq_list, name='enq_list'),
  path('create/<int:enq_id>/', views.create, name='create'),
  path('answer/<int:enq_id>/', views.answer, name='answer'),
  path('check/<int:enq_id>/', views.check, name='check'),
  path('end/', views.end, name='end'),
  path('question_delete/<int:enq_id>/<int:question_id>', views.question_delete, name='question_delete'),
]