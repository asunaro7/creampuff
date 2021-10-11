# /todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo, Category, MyWeapon, MyArmorHead, MyArmorUpper, MyArmorLower, User, User2
from .models_game import Game, Player
from .forms import TodoForm
from .forms_category import CategoryForm
from django.utils import timezone



"""一覧表示"""
def index(request):
    todo = Todo.objects.order_by('deadline_date')
    now = timezone.now

    content = {
        'todo': todo,
         'now':now,
         'Game':Game,
         'Player':Player,
         # 'mon':mon,
         # 'pl':pl,
    }
    return render(request, 'todo/index.html', content)

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

"""カテゴリー削除"""
def delete_category(request, id):
    category = get_object_or_404(Category,pk=id)
    category.delete()
    return redirect('todo:new_c')

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

#-------------------------------------------------------------------#
"""ゲーム"""
"""完了ボタン"""
def encount(request, id):
    todo = get_object_or_404(Todo,pk=id)
    field_name = 'level'
    field_value = getattr(todo, field_name)
    Game.mon = False
    Game.pl = False
    Game.task_counter += 1
    n = Game.n

    if Player.hp == 0:
        Player.hp = 1000

    if Game.monster[n][1] == 0:
        n += 1
        Game.n = n

    if todo.deadline_date > timezone.now(): #締め切りが間に合っている時
        Game.attack_name = Player.name
        Game.damage_name = Game.monster[n][0]
        Game.damage_a_hp = Game.monster[n][1]

        Game.attack_power = int(field_value) * 100
        Player.attack_sum += Game.attack_power
        Player.attack = Game.attack_power

        Game.damage_a_hp -= Game.attack_power
        if Game.damage_a_hp <= 0:
            Game.mon = True
            Game.monster[n][1] = 0
            Player.level += 1
        else:
            Game.monster[n][1] = Game.damage_a_hp

    else:                                      #締め切りがすぎている時
        Game.attack_name = Game.monster[n][0]
        Game.damage_name = Player.name
        Game.damage_a_hp = Player.hp

        Game.attack_power = Game.monster[n][2]

        Game.damage_a_hp -= Game.attack_power
        if Game.damage_a_hp <= 0:
            Game.pl = True
            Player.hp = 0
            Player.level = 0
        else:
            Player.hp = Game.damage_a_hp

        Player.attack = 0

    if Player.hp == 0:
        for monster in Game.monster:
            monster[1] = monster[3]

        Game.n = 0

    field_name_title = 'title'
    field_value_title = getattr(todo, field_name_title)
    Game.task.append(field_value_title)
    Game.task.append(field_value)

    Game.task_history.append(Game.task)

    Game.task.clear()
    
    todo.delete()

    return redirect('todo:index')

# """戦闘履歴"""
# def history():



#--------------------------------------------------------------#

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
    weapon = get_object_or_404(MyWeapon,pk=id)
    user = User.objects.first()

    weapon.num += 1
    user.money -= weapon.price
    user.save()
    weapon.save()

    return redirect('todo:buyEquipment')

"""キャラクタ表示"""
def dispCharData(request):
    name = Player.name
    hp = Player.hp
    money = Player.money
    level = Player.level

    weapon = Player.Weapon[0]
    armorHead = Player.ArmorHead[0]
    armorUpper = Player.ArmorUpper[0]
    armorLower = Player.ArmorLower[0]

    txt = {
       'name':name,
       'hp':hp,
       'money':money,
       'level':level,
       'weapon':weapon,
       'armorHead':armorHead,
       'armorUpper':armorUpper,
       'armorLower':armorLower,
    }
    return render(request, 'todo/dispCharData.html', txt)

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

    name = Player.name
    hp = Player.hp
    money = Player.money
    level = Player.level

    weapon = Player.Weapon[0]
    armorHead = Player.ArmorHead[0]
    armorUpper = Player.ArmorUpper[0]
    armorLower = Player.ArmorLower[0]

    txt2 = {
    'user': user11,
    'user2': user12,
    'wpn': wpn,
    'amrH': amrH,
    'amrU': amrU,
    'amrL': amrL,
    'name':name,
    'hp':hp,
    'money':money,
    'level':level,
    'weapon':weapon,
    'armorHead':armorHead,
    'armorUpper':armorUpper,
    'armorLower':armorLower,
    }
    #
    # name = Player.name
    # hp = Player.hp
    # money = Player.money
    # level = Player.level
    #
    # weapon = Player.Weapon[0]
    # armorHead = Player.ArmorHead[0]
    # armorUpper = Player.ArmorUpper[0]
    # armorLower = Player.ArmorLower[0]
    #
    # txt1 ={
    #     'name':name,
    #     'hp':hp,
    #     'money':money,
    #     'level':level,
    #     'weapon':weapon,
    #     'armorHead':armorHead,
    #     'armorUpper':armorUpper,
    #     'armorLower':armorLower,
    # }

    return render(request, 'todo/changeEquipment.html', txt2)

"""装備変更選択（武器）"""
def weaponSelect(request, id):
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
