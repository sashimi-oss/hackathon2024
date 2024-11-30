from django.contrib import admin

# Register your models here.

# モデルをインポート
from . models import Format, Item, Question, Enquete, Answer

# 管理ツールに登録
admin.site.register(Format)
admin.site.register(Item)
admin.site.register(Question)
admin.site.register(Enquete)
admin.site.register(Answer)