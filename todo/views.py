# /todo/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo, Category
from .forms import TodoForm
from django.utils import timezone


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

"""ゲーム"""
def encount(request, id):
    todo = get_object_or_404(Todo,pk=id)
    # obj = Todo.objects.first()
    field_name = 'level'
    field_value = getattr(todo, field_name)
    attack = int(field_value) * 100
    brave_name = '勇者くん'
    brave_HP = 100000
    monsterA_name = 'モンスターA'
    monsterA_HP = 10000
    monster_damageHP = monsterA_HP - attack
    context={
      'brave_name':brave_name,
      'brave_HP':brave_HP,
      'attack':attack,
      'monster_name':monsterA_name,
      'monster_HP':monsterA_HP,
      'monster_damageHP':monster_damageHP,
    }
    return render(request, 'todo/game.html', context)

def detail(request, pk):
    todos = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/detail.html', {'todos': todos})

"""登録フォーム"""
def new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo:detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todo/edit.html', {'form': form})

"""編集フォーム"""
def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo:detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/edit.html', {'form': form})
