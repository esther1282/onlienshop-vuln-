from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete', views.delete, name='delete'),
    path('<int:post_id>/modify', views.modify, name='modify'),
    path('index/', views.index, name='index'),
]