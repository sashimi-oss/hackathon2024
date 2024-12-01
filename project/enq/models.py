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
  question_id = models.AutoField(primary_key=True)
  question = models.TextField(verbose_name='質問')
  format = models.ForeignKey(Format, on_delete=models.CASCADE)
  order_no = models.IntegerField(default=0)
  # item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
  # answer = models.ForeignKey(Answer, null=True, on_delete=models.CASCADE)
  # answer = models.TextField(max_length=300, verbose_name='アンケート結果', null=True)
  enq = models.ForeignKey(Enquete, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.question
  
 
class Item(models.Model):
  item_id = models.AutoField(primary_key=True)
  question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='items')
  item = models.CharField(max_length=30, verbose_name='項目')

  def __str__(self):
    return self.item


class Answer(models.Model):
  answer_id = models.AutoField(primary_key=True)
  question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
  answer = models.TextField(max_length=300, verbose_name='アンケート結果', null=True, blank=True)
  enq = models.ForeignKey(Enquete, on_delete=models.CASCADE, default=0)
  
  def __str__(self):
    return self.answer[:50]