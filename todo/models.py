# /todo/models.py

from django.conf import settings
from django.db import models
from django.utils import timezone


"""カテゴリー"""
class Category(models.Model):
    title = models.CharField('タイトル', max_length=20)

    """self.titleとすることでadmin管理画面にてインスタンス変数として表示される"""
    def __str__(self):
        return self.title


"""
タイトル、日付テーブルとカテゴリーを紐づけるためのテーブル。
PROTECTは紐づいているデータが存在すれば消されない
"""
class Todo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField('タイトル', max_length=50)
    #text = models.TextField('詳細')
    created_date = models.DateTimeField('作成日',default=timezone.now)
    deadline_date = models.DateTimeField('締切日',blank=True, null=True)
    
    l_category = (
      ('1', '易'),
      ('2', 'やや易'),
      ('3', '普通'),
      ('4', 'やや難'),
      ('5', '難'),
    )
    level = models.CharField(
         '難易度(易 1〜5 難)',
         max_length=5,
         default='',
         choices=l_category
         )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
