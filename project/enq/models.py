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

class Item(models.Model):
  item1 = models.CharField(max_length=100, verbose_name='項目1', null=True, default='非常に満足')
  item2 = models.CharField(max_length=100, verbose_name='項目2', null=True, default='やや満足')
  item3 = models.CharField(max_length=100, verbose_name='項目3', null=True, default='少し満足')
  item4 = models.CharField(max_length=100, verbose_name='項目4', null=True, default='どちらともいえない')
  item5 = models.CharField(max_length=100, verbose_name='項目5', null=True, default='少し不満')
  item6 = models.CharField(max_length=100, verbose_name='項目6', null=True, default='やや不満')
  item7 = models.CharField(max_length=100, verbose_name='項目7', null=True, default='非常に不満')

  def __str__(self):
    return self.item
  
class Answer(models.Model):
  answer = models.TextField(max_length=300, verbose_name='アンケート結果', default='')

  def __str__(self):
    return self.answer

class Question(models.Model):
  id = models.AutoField(primary_key=True)
  question = models.TextField(verbose_name='質問')
  format_id = models.ForeignKey(Format, on_delete=models.CASCADE)
  order_no = models.IntegerField(default=0)
  item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
  # answer = models.ForeignKey(Answer, null=True, on_delete=models.CASCADE)
  answer = models.TextField(max_length=300, verbose_name='アンケート結果', null=True)
  enq_id = models.ForeignKey(Enquete, on_delete=models.CASCADE)
  

  def __str__(self):
    return self.question
  
