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


"""タスク内容"""
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

"""ゲーム:モンスター"""
class Game_monster(models.Model):
    name = models.CharField('名前', max_length=10)
    hp = models.PositiveIntegerField('HP')

    def __str__(self):
        return self.name

"""ゲーム:攻撃"""
class User(models.Model):
    brave_name = '勇者くん'
    attack = 0

    def __str__(self):
        return self.attack

"""キャラクタデータ"""
class CharData(models.Model):
    myName = models.CharField('名前',blank=True, null=True,default="", max_length=50)
    myHP = models.IntegerField('HP',blank=True, null=True,default=0)
    myLevel= models.IntegerField('レベル',blank=True, null=True,default=0)
    myWeapon = models.CharField('武器',blank=True, null=True,default="", max_length=50)
    myArmorHead  = models.CharField('防具　頭',blank=True, null=True,default="", max_length=50)
    myArmorUpper  = models.CharField('防具　上',blank=True, null=True,default="", max_length=50)
    myArmorLower  = models.CharField('防具　下',blank=True, null=True,default="", max_length=50)
    myArmorAccessory  = models.CharField('防具　アクセサリ',blank=True, null=True,default="", max_length=50)
    myMoney = models.IntegerField('持ち金',blank=True, null=True,default=0)

    l_category = (
      ('1', '易'),
      ('2', 'やや易'),
      ('3', '普通'),
      ('4', 'やや難'),
      ('5', '難'),
    )

    def __str__(self):
        return self.myName

"""所持武器データ"""
class MyWeapon(models.Model):
    myName = models.CharField('武器名',blank=True, null=True,default="", max_length=50)

    attackPower  = models.IntegerField('攻撃力',blank=True, null=True,default=0)
    defensePower  = models.IntegerField('防御力',blank=True, null=True,default=0)
    hpRecoveryPower  = models.IntegerField('HP回復力',blank=True, null=True,default=0)
    price  = models.IntegerField('購入額',blank=True, null=True,default=0)
    num  = models.IntegerField('所持数',blank=True, null=True,default=0)

    def __str__(self):
        return self.myName


"""所持防具データ"""
class MyArmorHead(models.Model):
    myName = models.CharField('防具名　頭',blank=True, null=True,default="", max_length=50)

    attackPower  = models.IntegerField('攻撃力',blank=True, null=True,default=0)
    defensePower  = models.IntegerField('防御力',blank=True, null=True,default=0)
    hpRecoveryPower  = models.IntegerField('HP回復力',blank=True, null=True,default=0)
    price  = models.IntegerField('購入額',blank=True, null=True,default=0)
    num  = models.IntegerField('所持数',blank=True, null=True,default=0)

    def __str__(self):
        return self.myName

"""所持防具データ"""
class MyArmorUpper(models.Model):
    myName = models.CharField('防具名　上',blank=True, null=True,default="", max_length=50)

    attackPower  = models.IntegerField('攻撃力',blank=True, null=True,default=0)
    defensePower  = models.IntegerField('防御力',blank=True, null=True,default=0)
    hpRecoveryPower  = models.IntegerField('HP回復力',blank=True, null=True,default=0)
    price  = models.IntegerField('購入額',blank=True, null=True,default=0)
    num  = models.IntegerField('所持数',blank=True, null=True,default=0)

    def __str__(self):
        return self.myName

"""所持防具データ"""
class MyArmorLower(models.Model):
    myName = models.CharField('防具名　下',blank=True, null=True,default="", max_length=50)

    attackPower  = models.IntegerField('攻撃力',blank=True, null=True,default=0)
    defensePower  = models.IntegerField('防御力',blank=True, null=True,default=0)
    hpRecoveryPower  = models.IntegerField('HP回復力',blank=True, null=True,default=0)
    price  = models.IntegerField('購入額',blank=True, null=True,default=0)
    num  = models.IntegerField('所持数',blank=True, null=True,default=0)

    def __str__(self):
        return self.myName
