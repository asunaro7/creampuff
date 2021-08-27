# /todo/admin.py

from django.contrib import admin
from .models import Category, Todo, Game_monster, CharData, MyWeapon, MyArmorHead, MyArmorUpper, MyArmorLower, CharData2

admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(Game_monster)
admin.site.register(CharData)
admin.site.register(MyWeapon)
admin.site.register(MyArmorHead)
admin.site.register(MyArmorUpper)
admin.site.register(MyArmorLower)
admin.site.register(CharData2)
