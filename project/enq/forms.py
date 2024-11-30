from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ['question', 'format_id', 'order_no']
    widgets = {
      'enq_id':forms.HiddenInput()
    }