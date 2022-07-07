from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "user"
urlpatterns=[
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.profile, name='profile'),
    path('<int:pk>/fileUpload/', views.fileUpload, name='fileUpload'),
    path('<int:pk>/change_pw/', views.change_pw, name='change_pw'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static 파일 경로 설정
if settings.DEBUG: # 👈 DEBUG=True일 때만,
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)