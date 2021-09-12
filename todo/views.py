# /todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
<<<<<<< HEAD
from .models import Todo, Category, Game_monster, User, User2, MyWeapon, MyArmorHead, MyArmorUpper, MyArmorLower
=======
from .models import Todo, Category, Game_monster, User, CharData, CharData2, MyWeapon, MyArmorHead, MyArmorUpper, MyArmorLower
>>>>>>> 2aa2e0eac509e3e97bf80cbb49944d92c5078c34
from .forms import TodoForm
from django.utils import timezone


"""一覧表示"""
def index(request):
    todo = Todo.objects.order_by('title')
    monster = Game_monster.objects.first()
    user = User.objects.first()

    user2 = User2.objects.first()
    return render(request, 'todo/index.html', {'todo': todo, 'user':user, 'monster':monster, 'user2':user2})
#    return render(request, 'todo/index.html', {'todo': todo, 'user':User, 'monster':monster})

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

"""ゲーム"""
"""完了ボタン"""
def encount(request, id):
    todo = get_object_or_404(Todo,pk=id)
    field_name = 'level'
    field_value = getattr(todo, field_name)
    user = User.objects.first()
    user.attack += int(field_value) * user.weapon.attackPower
    user.save()
    todo.delete()
    return redirect('todo:index')

"""開始ボタン"""
def start(request):
    monster = Game_monster.objects.first()
    user = User.objects.first()
    if monster.hp < 0 :
        monster.delete()
        monster = Game_monster.objects.first()
    monster.hp -= user.attack
    monster.save()
    user.attack = 0
    return redirect('todo:index')

"""武器購入画面表示"""
def buyEquipment(request):
#    todo = Todo.objects.order_by('title')
    weapon = MyWeapon.objects.order_by('myName')
    user = User.objects.first()
    return render(request, 'todo/buyEquipment.html', {'user': user,'weapon': weapon})

"""武器購入画面表示"""
def buyWeapon2(request):
#    todo = Todo.objects.order_by('title')
    weapon = MyWeapon.objects.order_by('myName')
    return render(request, 'todo/buyWeapon.html', {'weapon': weapon})

"""装備購入（武器）"""
def buyWeapon(request, id):
    from .models import User2
    weapon = get_object_or_404(MyWeapon,pk=id)
    user = User.objects.first()

    weapon.num += 1
    user.money -= weapon.price
    user.save()
    weapon.save()



#    user2 = User2.objects.first()
#    if weapon.num >= 1:
#        user2.weapon = weapon
#        user2.save()

#    wpn = MyWeapon.objects.order_by('myName')
#    amrH = MyArmorHead.objects.order_by('myName')
#    amrU = MyArmorUpper.objects.order_by('myName')
#    amrL = MyArmorLower.objects.order_by('myName')

#    return render(request, 'todo/buyWeapon.html', {'user': user,'user2': user2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})
    return redirect('todo:buyEquipment')

"""キャラクタ表示"""
def dispCharData(request):
    todo = User.objects.order_by('brave_name')
    return render(request, 'todo/dispCharData.html', {'todo': todo})

"""装備変更表示"""
def changeEquipment(request):
<<<<<<< HEAD
#    user = User.objects.order_by('brave_name')
#    user2 = User2.objects.order_by('brave_name')
    user11 = User.objects.first()
#    user11 = User.objects.get(pk=1)
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
=======
    cData = CharData.objects.order_by('myName')
    cData2 = CharData2.objects.order_by('myName')
    cData11 = CharData.objects.get(pk=1)
    print(CharData2.objects.count())
    if CharData2.objects.count() >= 1:
        cData12 = CharData2.objects.get(pk=1)
        cData12.myName = cData11.myName
        cData12.myWeapon = cData11.myWeapon
        cData12.myArmorHead = cData11.myArmorHead
        cData12.myArmorUpper = cData11.myArmorUpper
        cData12.myArmorLower = cData11.myArmorLower
        cData12.save()
    else:
        cData12 = CharData2.objects.create(id=1,myName="tairako",myArmorHead_id = 2,myArmorUpper_id = 2,myArmorLower_id = 2,myWeapon_id = 2)
        cData12.myName = cData11.myName
        cData12.myWeapon = cData11.myWeapon
        cData12.myArmorHead = cData11.myArmorHead
        cData12.myArmorUpper = cData11.myArmorUpper
        cData12.myArmorLower = cData11.myArmorLower
        cData12.save()
>>>>>>> 2aa2e0eac509e3e97bf80cbb49944d92c5078c34

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')
<<<<<<< HEAD
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
=======
    return render(request, 'todo/changeEquipment.html', {'charData': cData11,'charData2': cData12, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})

"""装備変更選択（武器）"""
def weaponSelect(request, id):
    from .models import CharData2
    weapon = get_object_or_404(MyWeapon,pk=id)
    cData = CharData.objects.get(pk=1)
    cData2 = CharData2.objects.get(pk=1)
    if weapon.num >= 1:
        cData2.myWeapon = weapon
        cData2.save()
>>>>>>> 2aa2e0eac509e3e97bf80cbb49944d92c5078c34

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

<<<<<<< HEAD
    return render(request, 'todo/changeEquipment.html', {'user': user,'user2': user2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})
#    return redirect('todo:changeEquipment')

"""装備変更選択（防具　頭）"""
def armorHeadSelect(request, id):
    from .models import User2
    armorHead = get_object_or_404(MyArmorHead,pk=id)
    user = User.objects.first()
    user2 = User2.objects.first()
    if armorHead.num >= 1:
        user2.armorHead = armorHead
        user2.save()
=======
    return render(request, 'todo/changeEquipment.html', {'charData': cData,'charData2': cData2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})

"""装備変更選択（防具　頭）"""
def armorHeadSelect(request, id):
    from .models import CharData2
    armorHead = get_object_or_404(MyArmorHead,pk=id)
    cData = CharData.objects.get(pk=1)
    cData2 = CharData2.objects.get(pk=1)
    if armorHead.num >= 1:
        cData2.myArmorHead = armorHead
        cData2.save()
>>>>>>> 2aa2e0eac509e3e97bf80cbb49944d92c5078c34

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

<<<<<<< HEAD
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
=======
    return render(request, 'todo/changeEquipment.html', {'charData': cData,'charData2': cData2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})

"""装備変更選択（防具　上）"""
def armorUpperSelect(request, id):
    from .models import CharData2
    armorUpper = get_object_or_404(MyArmorUpper,pk=id)
    cData = CharData.objects.get(pk=1)
    cData2 = CharData2.objects.get(pk=1)
    if armorUpper.num >= 1:
        cData2.myArmorUpper = armorUpper
        cData2.save()
>>>>>>> 2aa2e0eac509e3e97bf80cbb49944d92c5078c34

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

<<<<<<< HEAD
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
=======
    return render(request, 'todo/changeEquipment.html', {'charData': cData,'charData2': cData2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})

"""装備変更選択（防具　下）"""
def armorLowerSelect(request, id):
    from .models import CharData2
    armorLower = get_object_or_404(MyArmorLower,pk=id)
    cData = CharData.objects.get(pk=1)
    cData2 = CharData2.objects.get(pk=1)
    if armorLower.num >= 1:
        cData2.myArmorLower = armorLower
        cData2.save()
>>>>>>> 2aa2e0eac509e3e97bf80cbb49944d92c5078c34

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')

<<<<<<< HEAD
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
=======
    return render(request, 'todo/changeEquipment.html', {'charData': cData,'charData2': cData2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})

"""装備変更完了"""
def changeComplete(request):
    cData = CharData.objects.get(pk=1)
    cData2 = CharData2.objects.get(pk=1)
    cData.myWeapon = cData2.myWeapon
    cData.myArmorHead = cData2.myArmorHead
    cData.myArmorUpper = cData2.myArmorUpper
    cData.myArmorLower = cData2.myArmorLower
    cData.save()
>>>>>>> 2aa2e0eac509e3e97bf80cbb49944d92c5078c34

    wpn = MyWeapon.objects.order_by('myName')
    amrH = MyArmorHead.objects.order_by('myName')
    amrU = MyArmorUpper.objects.order_by('myName')
    amrL = MyArmorLower.objects.order_by('myName')
<<<<<<< HEAD
#    return render(request, 'todo/changeEquipment.html', {'user': user,'user2': user2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})
    return redirect('todo:dispCharData')
#    return render(request)
#    return render(request, 'todo/dispCharData.html', {'todo': todo})
=======
    return render(request, 'todo/changeEquipment.html', {'charData': cData,'charData2': cData2, 'wpn': wpn, 'amrH': amrH, 'amrU': amrU, 'amrL': amrL})
>>>>>>> 2aa2e0eac509e3e97bf80cbb49944d92c5078c34
