# /todo/admin.py

from django.contrib import admin
<<<<<<< HEAD
from .models import Category, Todo, Game_monster, MyWeapon, MyArmorHead, MyArmorUpper, MyArmorLower,User,User2
=======
from .models import Category, Todo, Game_monster, CharData, MyWeapon, MyArmorHead, MyArmorUpper, MyArmorLower, CharData2
>>>>>>> 2aa2e0eac509e3e97bf80cbb49944d92c5078c34

admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(Game_monster)
admin.site.register(MyWeapon)
admin.site.register(MyArmorHead)
admin.site.register(MyArmorUpper)
admin.site.register(MyArmorLower)
<<<<<<< HEAD
admin.site.register(User)
admin.site.register(User2)
=======
admin.site.register(CharData2)
>>>>>>> 2aa2e0eac509e3e97bf80cbb49944d92c5078c34
