from django.db import models

class Format(models.Model):
  format_id = models.AutoField(primary_key=True)
  format = models.CharField(max_length=20, verbose_name='形式')

  def __str__(self):
    return self.format

class Question(models.Model):
  id = models.AutoField(primary_key=True)
  question = models.TextField(verbose_name='質問')
  format_id = models.ForeignKey(Format, on_delete=models.CASCADE)
  order_id = models.IntegerField(default=0)

  def __str__(self):
    return self.question
