# /todo/urls.py

from django.urls import path
from . import views
from django.conf.urls.static import static #追加
from django.conf import settings #追加

app_name = 'todo'

urlpatterns = [
        path('', views.index, name='index'),  # ←一覧
        path('<int:id>/delete/', views.delete, name='delete'),  # ←削除機能用

        path('todo/<str:category>/', views.todo_category, name='todo_category'),  # ←カテゴリ
        path('category/form/', views.new_c, name='new_c'), # ←　カテゴリー追加
        path('category/form/<int:pk>/', views.detail_c, name='detail_c'),

        path('<int:id>/game/', views.encount, name='encount'), # ←ゲーム

        path('form/', views.new, name='new'), #　←タスク追加
        path('form/<int:pk>/', views.detail, name='detail'),
        path('form/<int:pk>/edit/', views.edit, name='edit'),

        path('buyWeapon2', views.buyWeapon2, name='buyWeapon2'),    # ←追加

        path('dispCharData', views.dispCharData, name='dispCharData'),    # ←追加
        path('changeEquipment', views.changeEquipment, name='changeEquipment'),    # ←追加
        
        path('<int:id>/buyWeapon/', views.buyWeapon, name='buyWeapon'),    # ←追加
        path('<int:id>/weaponSelect/', views.weaponSelect, name='weaponSelect'),    # ←追加
        path('<int:id>/armorHeadSelect/', views.armorHeadSelect, name='armorHeadSelect'),    # ←追加
        path('<int:id>/armorUpperSelect/', views.armorUpperSelect, name='armorUpperSelect'),    # ←追加
        path('<int:id>/armorLowerSelect/', views.armorLowerSelect, name='armorLowerSelect'),    # ←追加
        path('changeComplete', views.changeComplete, name='changeComplete'),    # ←追加

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #追加
