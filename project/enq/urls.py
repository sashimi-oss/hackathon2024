from django.urls import path
from . import views

app_name = 'enq'
urlpatterns = [
  path('', views.index, name='index'),
  path('', views.create, name='create'),
  path('', views.check, name='check'),
]