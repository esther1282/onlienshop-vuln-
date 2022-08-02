from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.db import connection
from django.contrib.auth.hashers import check_password

def index(request):
    try:
        username = request.COOKIES['username']
        return render(request, 'master/index.html')
    except:
        return redirect('master:login')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user:
            response = redirect('master:index')
            response.set_cookie(key='username', value=user.username)
            return response
        else:
            cursor = connection.cursor()
            strSql = "SELECT username FROM user_user where email='"+email+"' and password='"+password+"'"
            print(strSql)
            cursor.execute(strSql)
            datas = cursor.fetchall()
            if datas:
                response = redirect('master:index')
                response.set_cookie(key='username', value='First_User')
                return response
        return render(request, 'master/login.html', {'form': LoginForm()})
    else:
        form = LoginForm()
        return render(request, 'master/login.html', {'form': form})

def logout(request):
    response = redirect('/master/login')
    response.delete_cookie(key='username')
    return response
