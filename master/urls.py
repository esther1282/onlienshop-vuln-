from django.urls import path
from . import views

app_name = "master"
urlpatterns=[
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.login, name='logout'),
]