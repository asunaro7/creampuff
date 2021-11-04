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

"""タスクログデータ"""
class TaskLog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField('タイトル', max_length=50)
    #text = models.TextField('詳細')
    taskNo = models.IntegerField('タスクＮＯ',blank=True, null=True,default=1)
    taskCompNum = models.IntegerField('タスク完了数',blank=True, null=True,default=0)
    created_date = models.DateTimeField('作成日',default=timezone.now)
    deadline_date = models.DateTimeField('締切日',blank=True, null=True)
    complete_date = models.DateTimeField('完了日',blank=True, null=True)
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

    def __str__(self):
        return self.title

"""バトルログデータ"""
class BattleLog(models.Model):
    name = models.CharField('モンスター名', max_length=50)
    battle = models.CharField('攻防', max_length=50)
    hp = models.IntegerField('モンスターＨＰ',blank=True, null=True,default=1)
    attackPower = models.IntegerField('モンスター攻撃力',blank=True, null=True,default=1)
    damegeHp = models.IntegerField('モンスターダメージ',blank=True, null=True,default=1)
    complete_date = models.DateTimeField('完了日',blank=True, null=True)

    pName = models.CharField('プレイヤー名', max_length=50)
    pHp = models.IntegerField('プレイヤーＨＰ',blank=True, null=True,default=1)
    pMoney = models.IntegerField('プレイヤー持ち金',blank=True, null=True,default=1)
    pLevel = models.IntegerField('プレイヤーレベル',blank=True, null=True,default=1)

    def __str__(self):
        return self.name

"""キャラクタデータ"""
"""
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
        return self.myName"""

"""所持武器データ"""
class MyWeapon(models.Model):
    myName = models.CharField('武器名',blank=True, null=True,default="", max_length=50)
    attackPower  = models.IntegerField('攻撃力',blank=True, null=True,default=100)
    defensePower  = models.IntegerField('防御力',blank=True, null=True,default=0)
    hpRecoveryPower  = models.IntegerField('HP回復力',blank=True, null=True,default=0)
    price  = models.IntegerField('購入額',blank=True, null=True,default=100)
    num  = models.IntegerField('所持数',blank=True, null=True,default=0)

    def __str__(self):
        return self.myName


"""所持防具データ"""
class MyArmorHead(models.Model):
    myName = models.CharField('防具名　頭',blank=True, null=True,default="", max_length=50)
    attackPower  = models.IntegerField('攻撃力',blank=True, null=True,default=0)
    defensePower  = models.IntegerField('防御力',blank=True, null=True,default=100)
    hpRecoveryPower  = models.IntegerField('HP回復力',blank=True, null=True,default=10)
    price  = models.IntegerField('購入額',blank=True, null=True,default=100)
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

"""ゲーム:攻撃"""
class User(models.Model):
    brave_name = models.CharField('名前',blank=True, null=True,default="勇者くん", max_length=50)
    hp = models.IntegerField('HP',blank=True, null=True,default=100)
    weapon = models.ForeignKey(MyWeapon,verbose_name = '武器', on_delete = models.PROTECT,default="木刀")
    armorHead  = models.ForeignKey(MyArmorHead,verbose_name = '防具　頭', on_delete = models.PROTECT,default="布の帽子")
    armorUpper  = models.ForeignKey(MyArmorUpper,verbose_name = '防具　上', on_delete = models.PROTECT,default="衣上")
    armorLower  = models.ForeignKey(MyArmorLower,verbose_name = '防具　下', on_delete = models.PROTECT,default="衣下")
    level= models.IntegerField('レベル',blank=True, null=True,default=1)
    money = models.IntegerField('持ち金',blank=True, null=True,default=1000)

    def __str__(self):
        return self.brave_name

"""ゲーム:攻撃"""
class User2(models.Model):
    brave_name = models.CharField('名前',blank=True, null=True,default="勇者くん", max_length=50)
    hp = models.IntegerField('HP',blank=True, null=True,default=100)

    weapon = models.ForeignKey(MyWeapon,verbose_name = '武器', on_delete = models.PROTECT,default="木刀")
    armorHead  = models.ForeignKey(MyArmorHead,verbose_name = '防具　頭', on_delete = models.PROTECT,default="布の帽子")
    armorUpper  = models.ForeignKey(MyArmorUpper,verbose_name = '防具　上', on_delete = models.PROTECT,default="衣上")
    armorLower  = models.ForeignKey(MyArmorLower,verbose_name = '防具　下', on_delete = models.PROTECT,default="衣下")
    level= models.IntegerField('レベル',blank=True, null=True,default=1)
    money = models.IntegerField('持ち金',blank=True, null=True,default=1000)

    def __str__(self):
        return self.brave_name
