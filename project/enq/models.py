from django.db import models

class Enquete(models.Model):
  enq_id = models.AutoField(primary_key=True)#アンケート識別
  title = models.CharField(max_length=50, verbose_name='アンケートタイトル')

  def __str__(self):
    return self.title

class Format(models.Model):
  format_id = models.IntegerField(primary_key=True)
  format = models.CharField(max_length=20, verbose_name='形式')

  def __str__(self):
    return self.format

class Question(models.Model):
  id = models.AutoField(primary_key=True)
  question = models.TextField(verbose_name='質問')
  format_id = models.ForeignKey(Format, on_delete=models.CASCADE)
  order_no = models.IntegerField(default=0)
  enq_id = models.ForeignKey(Enquete, on_delete=models.CASCADE)

  def __str__(self):
    return self.question
