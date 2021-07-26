# /todo/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo, Category


"""一覧表示"""
def index(request):
    todo = Todo.objects.order_by('title')
    return render(request, 'todo/index.html', {'todo': todo})


"""削除機能"""#タスクを削除する場合
def delete(request, id):
    todo = get_object_or_404(Todo,pk=id)
    todo.delete()
    return redirect('todo:index')


"""カテゴリ"""
def todo_category(request, category):
    category = Category.objects.get(title=category)
    """カテゴリで絞り込む"""
    todo = Todo.objects.filter(category=category).order_by('title')
    return render(request, 'todo/index.html', {'todo': todo, 'category': category})

"""ゲーム初期"""
def encount(request, id):
    todo = get_object_or_404(Todo,pk=id)
    field_name = 'level'
    field_value = getattr(todo, field_name)
    attack = int(field_value) * 100
    monsterA_name = 'モンスターA'
    monsterA_HP = 10000
    return HttpResponse(monsterA_name + " へ "+str(attack)+" の こうげき！ "
                         + monsterA_name + " の HP は " + str(monsterA_HP-attack) + " に なった。 ")
