# /todo/admin.py

from django.contrib import admin
from .models import Category, Todo, Game_monster

admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(Game_monster)
