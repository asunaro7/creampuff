# /todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo, Category, MyWeapon, MyArmorHead, MyArmorUpper, MyArmorLower, User, User2
from .models_game import Game, Player, Manekin
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
    Game.deadlineFlg = 0

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

        Game.deadlineFlg = 1

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

"""締め切り日時オーバー"""
def deadline_date(request):
    todo = Todo.objects.order_by('title')
    user = User.objects.first()
    user.hp -= 1000
    user.save()

#    return redirect('todo:index')
    return redirect('todo:index', {'user': user})

#"""武器購入画面表示"""
#def buyWeapon2(request):
    #todo = Todo.objects.order_by('title')
    #return render(request, 'todo/buyWeapon.html', {'todo': todo})

"""武器購入画面表示"""
def buyEquipment(request):
    weapon = MyWeapon.objects.order_by('myName')
    user = User.objects.first()
    return render(request, 'todo/buyEquipment.html', {'user': user,'weapon': weapon})

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
    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

    name = Player.name
    hp = Player.hp
    money = Player.money
    level = Player.level

    Manekin.Weapon[0] = Player.Weapon[0]
    Manekin.ArmorHead[0] = Player.ArmorHead[0]
    Manekin.ArmorUpper[0] = Player.ArmorUpper[0]
    Manekin.ArmorLower[0] = Player.ArmorLower[0]

    txt2 = {
    'wpn': wpn,
    'amrH': amrH,
    'amrU': amrU,
    'amrL': amrL,

    'name':name,
    'hp':hp,
    'money':money,
    'level':level,

    'P_weapon':Player.Weapon[0],
    'P_armorHead':Player.ArmorHead[0],
    'P_armorUpper':Player.ArmorUpper[0],
    'P_armorLower':Player.ArmorLower[0],

    'M_weapon':Manekin.Weapon[0],
    'M_armorHead':Manekin.ArmorHead[0],
    'M_armorUpper':Manekin.ArmorUpper[0],
    'M_armorLower':Manekin.ArmorLower[0],
    }
    return render(request, 'todo/changeEquipment.html', txt2)

"""装備変更選択（武器）"""
def weaponSelect(request, id):
    weapon = get_object_or_404(MyWeapon,pk=id)

    if weapon.num >= 1:
        Manekin.Weapon[0] = weapon.myName
        Manekin.Weapon[1] = weapon.attackPower
        Manekin.Weapon[2] = weapon.defensePower
        Manekin.Weapon[3] = weapon.hpRecoveryPower
        Manekin.Weapon[4] = weapon.price
        Manekin.Weapon[5] = weapon.num

    name = Player.name
    hp = Player.hp
    money = Player.money
    level = Player.level

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

    txt2 = {
    'wpn': wpn,
    'amrH': amrH,
    'amrU': amrU,
    'amrL': amrL,

    'name':name,
    'hp':hp,
    'money':money,
    'level':level,

    'P_weapon':Player.Weapon[0],
    'P_armorHead':Player.ArmorHead[0],
    'P_armorUpper':Player.ArmorUpper[0],
    'P_armorLower':Player.ArmorLower[0],

    'M_weapon':Manekin.Weapon[0],
    'M_armorHead':Manekin.ArmorHead[0],
    'M_armorUpper':Manekin.ArmorUpper[0],
    'M_armorLower':Manekin.ArmorLower[0],
    }

    return render(request, 'todo/changeEquipment.html', txt2)

"""装備変更選択（防具　頭）"""
def armorHeadSelect(request, id):
    armorHead = get_object_or_404(MyArmorHead,pk=id)

    if armorHead.num >= 1:
        Manekin.ArmorHead[0] = armorHead.myName
        Manekin.ArmorHead[1] = armorHead.attackPower
        Manekin.ArmorHead[2] = armorHead.defensePower
        Manekin.ArmorHead[3] = armorHead.hpRecoveryPower
        Manekin.ArmorHead[4] = armorHead.price
        Manekin.ArmorHead[5] = armorHead.num

    name = Player.name
    hp = Player.hp
    money = Player.money
    level = Player.level

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

    txt2 = {
    'wpn': wpn,
    'amrH': amrH,
    'amrU': amrU,
    'amrL': amrL,

    'name':name,
    'hp':hp,
    'money':money,
    'level':level,

    'P_weapon':Player.Weapon[0],
    'P_armorHead':Player.ArmorHead[0],
    'P_armorUpper':Player.ArmorUpper[0],
    'P_armorLower':Player.ArmorLower[0],

    'M_weapon':Manekin.Weapon[0],
    'M_armorHead':Manekin.ArmorHead[0],
    'M_armorUpper':Manekin.ArmorUpper[0],
    'M_armorLower':Manekin.ArmorLower[0],
    }

    return render(request, 'todo/changeEquipment.html', txt2)

"""装備変更選択（防具　上）"""
def armorUpperSelect(request, id):
    armorUpper = get_object_or_404(MyArmorUpper,pk=id)

    if armorUpper.num >= 1:
        Manekin.ArmorUpper[0] = armorUpper.myName
        Manekin.ArmorUpper[1] = armorUpper.attackPower
        Manekin.ArmorUpper[2] = armorUpper.defensePower
        Manekin.ArmorUpper[3] = armorUpper.hpRecoveryPower
        Manekin.ArmorUpper[4] = armorUpper.price
        Manekin.ArmorUpper[5] = armorUpper.num

    name = Player.name
    hp = Player.hp
    money = Player.money
    level = Player.level

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

    txt2 = {
    'wpn': wpn,
    'amrH': amrH,
    'amrU': amrU,
    'amrL': amrL,

    'name':name,
    'hp':hp,
    'money':money,
    'level':level,

    'P_weapon':Player.Weapon[0],
    'P_armorHead':Player.ArmorHead[0],
    'P_armorUpper':Player.ArmorUpper[0],
    'P_armorLower':Player.ArmorLower[0],

    'M_weapon':Manekin.Weapon[0],
    'M_armorHead':Manekin.ArmorHead[0],
    'M_armorUpper':Manekin.ArmorUpper[0],
    'M_armorLower':Manekin.ArmorLower[0],
    }

    return render(request, 'todo/changeEquipment.html', txt2)

"""装備変更選択（防具　下）"""
def armorLowerSelect(request, id):
    armorLower = get_object_or_404(MyArmorLower,pk=id)

    if armorLower.num >= 1:
        Manekin.ArmorLower[0] = armorLower.myName
        Manekin.ArmorLower[1] = armorLower.attackPower
        Manekin.ArmorLower[2] = armorLower.defensePower
        Manekin.ArmorLower[3] = armorLower.hpRecoveryPower
        Manekin.ArmorLower[4] = armorLower.price
        Manekin.ArmorLower[5] = armorLower.num

    name = Player.name
    hp = Player.hp
    money = Player.money
    level = Player.level

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

    txt2 = {
    'wpn': wpn,
    'amrH': amrH,
    'amrU': amrU,
    'amrL': amrL,

    'name':name,
    'hp':hp,
    'money':money,
    'level':level,

    'P_weapon':Player.Weapon[0],
    'P_armorHead':Player.ArmorHead[0],
    'P_armorUpper':Player.ArmorUpper[0],
    'P_armorLower':Player.ArmorLower[0],

    'M_weapon':Manekin.Weapon[0],
    'M_armorHead':Manekin.ArmorHead[0],
    'M_armorUpper':Manekin.ArmorUpper[0],
    'M_armorLower':Manekin.ArmorLower[0],
    }

    return render(request, 'todo/changeEquipment.html', txt2)

"""装備変更完了"""
def changeComplete(request):
    for i in range(6):
        Player.Weapon[i] = Manekin.Weapon[i]
        Player.ArmorHead[i] = Manekin.ArmorHead[i]
        Player.ArmorUpper[i] = Manekin.ArmorUpper[i]
        Player.ArmorLower[i] = Manekin.ArmorLower[i]
    return redirect('todo:dispCharData')





"""武器購入"""
def weapurchase(request):
    dic = [{'name':'ダイヤの剣','power':1000,'recov':0,'price':1000},
    {'name':'武器2','power':2000,'recov':200,'price':2000}]

    

    context={
      'w0':dic[0],
      'w1':dic[1],


    }

    return render(request, 'todo/weapurchase.html', context)
