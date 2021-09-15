# /todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo, Category, Game_monster, User, User2, MyWeapon, CharData, MyArmorHead, MyArmorUpper, MyArmorLower, task_counter
from .forms import TodoForm
from .forms_category import CategoryForm
from django.utils import timezone


"""一覧表示"""
def index(request):
    todo = Todo.objects.order_by('deadline_date')
    now = timezone.now
    monster_name = Game_monster.monster[0][0]
    monster_hp = Game_monster.monster[0][1]
    monster_attack = Game_monster.monster_attack
    user = User.objects.first()
    user2 = User2.objects.first()
    return render(request, 'todo/index.html',
                  {'todo': todo,
                   'now':now,
                   'user':user,
                   'user2':User2,
                   'monster_name':monster_name,
                   'monster_hp':monster_hp,
                   'monster_attack':monster_attack,
                   'task':task_counter,
                  })

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
    return render(request, 'todo/edit.html', {
    'form': form})

"""カテゴリー表示"""
def detail_c(request, pk):
    categorys = get_object_or_404(Category, pk=pk)
    return render(request, 'todo/detail_c.html', {'categorys': categorys})

"""カテゴリーフォーム"""
def new_c(request):
    if request.method == "POST":
        form_c = CategoryForm(request.POST)
        if form_c.is_valid():
            category = form_c.save(commit=False)
            category.save()
            return redirect('todo:detail_c', pk=category.pk)
    else:
        form_c = CategoryForm()
    return render(request, 'todo/new_c.html',{'forms':form_c})

"""ゲーム"""
"""完了ボタン"""
def encount(request, id):
    todo = get_object_or_404(Todo,pk=id)
    field_name = 'level'
    field_value = getattr(todo, field_name)
    user = User.objects.first()
    User.attack += int(field_value) * user.weapon.attackPower
    User.attack_sum += User.attack
    task_counter.counter += 1
    user.save()
    todo.delete()
    return redirect('todo:index')

"""開始ボタン"""
def start(request):
    monster_name = Game_monster.monster[0][0]
    monster_hp = Game_monster.monster[0][1]
    monster_hp -= User.attack
    Game_monster.monster[0][1] = monster_hp
    User.attack = 0
    return redirect('todo:index')

"""武器購入画面表示"""
def buyEquipment(request):
    weapon = MyWeapon.objects.order_by('myName')
    user = User.objects.first()
    return render(request, 'todo/buyEquipment.html', {'user': user,'weapon': weapon})

"""武器購入画面表示"""
def buyWeapon2(request):
    todo = Todo.objects.order_by('title')
    return render(request, 'todo/buyWeapon.html', {'todo': todo})

"""装備購入（武器）"""
def buyWeapon(request, id):
    from .models import User2
    weapon = get_object_or_404(MyWeapon,pk=id)
    user = User.objects.first()

    weapon.num += 1
    user.money -= weapon.price
    user.save()
    weapon.save()

    return redirect('todo:buyEquipment')

"""キャラクタ表示"""
def dispCharData(request):
    todo = User.objects.order_by('brave_name')
    return render(request, 'todo/dispCharData.html', {'todo': todo})

"""装備変更表示"""
def changeEquipment(request):
    user11 = User.objects.first()
    print(User.objects.count())
    if User2.objects.count() >= 1:
        user12 = User2.objects.first()
        user12.brave_name = user11.brave_name
        user12.weapon = user11.weapon
        user12.armorHead = user11.armorHead
        user12.armorUpper = user11.armorUpper
        user12.armorLower = user11.armorLower
        user12.save()
    else:
        user12 = User2.objects.create(id=1,brave_name="勇者くん",armorHead_id = 2,armorUpper_id = 2,armorLower_id = 2,weapon_id = 2)
        user12.brave_name = user11.brave_name
        user12.weapon = user11.weapon
        user12.armorHead = user11.armorHead
        user12.armorUpper = user11.armorUpper
        user12.armorLower = user11.armorLower
        user12.save()

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')
    return render(request, 'todo/changeEquipment.html', {'user': user11,'user2': user12, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})

"""装備変更選択（武器）"""
def weaponSelect(request, id):
    from .models import User2
    weapon = get_object_or_404(MyWeapon,pk=id)
    user = User.objects.first()
    user2 = User2.objects.first()
    if weapon.num >= 1:
        user2.weapon = weapon
        user2.save()

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

    return render(request, 'todo/changeEquipment.html', {'user': user,'user2': user2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})

"""装備変更選択（防具　頭）"""
def armorHeadSelect(request, id):
    from .models import User2
    armorHead = get_object_or_404(MyArmorHead,pk=id)
    user = User.objects.first()
    user2 = User2.objects.first()
    if armorHead.num >= 1:
        user2.armorHead = armorHead
        user2.save()

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

    return render(request, 'todo/changeEquipment.html', {'user': user,'user2': user2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})

"""装備変更選択（防具　上）"""
def armorUpperSelect(request, id):
    from .models import User2
    armorUpper = get_object_or_404(MyArmorUpper,pk=id)
    user = User.objects.first()
    user2 = User2.objects.first()
    if armorUpper.num >= 1:
        user2.armorUpper = armorUpper
        user2.save()

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

    return render(request, 'todo/changeEquipment.html', {'user': user,'user2': user2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})

"""装備変更選択（防具　下）"""
def armorLowerSelect(request, id):
    from .models import User2
    armorLower = get_object_or_404(MyArmorLower,pk=id)
    user = User.objects.first()
    user2 = User2.objects.first()
    if armorLower.num >= 1:
        user2.armorLower = armorLower
        user2.save()

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

    return render(request, 'todo/changeEquipment.html', {'user': user,'user2': user2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})

"""装備変更完了"""
def changeComplete(request):
    user = User.objects.first()
    user2 = User2.objects.first()
    user.weapon = user2.weapon
    user.armorHead = user2.armorHead
    user.armorUpper = user2.armorUpper
    user.armorLower = user2.armorLower
    user.save()

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')
    return redirect('todo:dispCharData')
