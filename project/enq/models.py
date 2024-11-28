from django.db import models


class Question(models.Model):
  id = models.AutoField(primary_key=True)
  question = models.TextField(verbose_name='質問')
  format_id = models.IntegerField()
  order_id = models.IntegerField()

class Format(models.Model):
  format_id = models.IntegerField(default=0)
  format = models.CharField(max_length=200, verbose_name='形式')