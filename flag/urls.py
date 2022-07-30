from django.urls import path
from . import views

app_name = "flag"
urlpatterns=[
    path('', views.index, name='index'),
]