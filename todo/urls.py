# /todo/urls.py

from django.urls import path
from . import views


app_name = 'todo'

urlpatterns = [
        path('', views.index, name='index'),  # ←一覧
        path('<int:id>/delete/', views.delete, name='delete'),  # ←削除機能用
        path('todo/<str:category>/', views.todo_category, name='todo_category'),  # ←カテゴリ
        path('<int:id>/game/', views.encount, name='encount'),
        path('form/', views.new, name='new'),
        path('form/<int:pk>/', views.detail, name='detail'),
        path('form/<int:pk>/edit/', views.edit, name='edit'),
]
