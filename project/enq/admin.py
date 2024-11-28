from django.contrib import admin

# Register your models here.

# モデルをインポート
from . models import Format, Question

# 管理ツールに登録
admin.site.register(Format)
admin.site.register(Question)