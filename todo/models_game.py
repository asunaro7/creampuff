from django.conf import settings
from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = '勇者くん1'
    hp = 1000000
    money = 100
    level = 1

    attack = 0
    attack_sum = 0

    #[名前,攻撃力,防御力,HP回復力,購入額,所持数]
    Weapon = ['普通の剣',10,0,0,0,1]
    ArmorHead = ['普通の兜',0,5,0,0,1]
    ArmorUpper = ['普通の鎧・上',0,5,0,0,1]
    ArmorLower = ['普通の鎧・下',0,5,0,0,1]

class Game(models.Model):
    task_counter = 0
    #[名前,HP,攻撃力]
    monster = [
      ['モンスターA', 1000, 10],
      ['モンスターB', 10000, 50],
      ['モンスターC', 100000, 100],
      ['モンスターD', 1000000, 200],
    ]

    attack_name = Player.name
    damage_name = monster[0][0]

    attack_power = 0
    damage_a_hp = monster[0][1]
