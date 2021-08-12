# /todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo, Category, Game_monster, User, CharData, MyWeapon, MyArmorHead, MyArmorUpper, MyArmorLower
from .forms import TodoForm
from django.utils import timezone


"""一覧表示"""
def index(request):
    todo = Todo.objects.order_by('title')
    monster = Game_monster.objects.first()
    return render(request, 'todo/index.html', {'todo': todo, 'user':User, 'monster':monster})

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

"""タスク内容表示"""
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

"""ゲーム"""
"""完了ボタン"""
def encount(request, id):
    todo = get_object_or_404(Todo,pk=id)
    field_name = 'level'
    field_value = getattr(todo, field_name)
    User.attack += int(field_value) * 100
    todo.delete()
    return redirect('todo:index')

"""開始ボタン"""
def start(request):
    monster = Game_monster.objects.first()
    if monster.hp < 0 :
        monster.delete()
        monster = Game_monster.objects.first()
    monster.hp -= User.attack
    monster.save()
    User.attack = 0
    return redirect('todo:index')

"""武器購入画面表示"""
def buyWeapon2(request):
    todo = Todo.objects.order_by('title')
    return render(request, 'todo/buyWeapon.html', {'todo': todo})

"""キャラクタ表示"""
def dispCharData(request):
    todo = CharData.objects.order_by('myName')
    return render(request, 'todo/dispCharData.html', {'todo': todo})

"""装備変更表示"""
def changeEquipment(request):
    cData = CharData.objects.order_by('myName')
    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')
    return render(request, 'todo/changeEquipment.html', {'charData': cData, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})
