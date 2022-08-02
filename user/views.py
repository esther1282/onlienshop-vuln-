from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import models, authenticate, get_user_model, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .forms import SignUpForm, CustomUserChangeForm, CheckPasswordForm, CustomPasswordChangeForm, FileUploadForm
from .models import User, Profile_image

from PIL import ImageMath

@require_http_methods(['GET', 'POST'])
def login(request):
    redirect_to = request.POST.get('next', '/')
    if request.method == "POST":
        next = request.POST.get('next', '/')
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, '로그인 성공')
            return HttpResponseRedirect(next)
        else:
            messages.error(request, '로그인 실패')
            return render(request, 'user/login.html', {'po_email': email})
    else:
        return render(request, 'user/login.html')

@require_http_methods(['GET', 'POST'])
def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                auth_login(request, user)
                messages.success(request, '회원 가입 성공')
                return HttpResponseRedirect(reverse('shop:index'))
        messages.error(request, '회원 가입 실패')
        context = {
            'form': form,
            'po_email': request.POST['email'],
            'po_username': request.POST['username'],
            'po_pw1': request.POST['password1'],
            'po_pw2': request.POST['password2']}
        return render(request, 'user/signup.html', context)
    else:
        form = SignUpForm()

    return render(request, 'user/signup.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, '로그아웃 완료')
    print("?")
    return redirect(request.META.get('HTTP_REFERER'))

def profile(request, pk):
    user = User.objects.get(id=pk)
    try:
        image = Profile_image.objects.filter(user=user).order_by('id').reverse()[0]
    except:
        image = ''
    fileform = FileUploadForm()

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, '업데이트 성공')
            return HttpResponseRedirect(reverse('user:profile', args=[pk]))
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, 'user/profile.html', {'form':form, 'fileform':fileform,'image':image})

@require_http_methods(['GET', 'POST'])
def fileUpload(request, pk):
    if request.method == 'POST':
        try:
            img = request.FILES["image"]
            title = request.POST['title']
            if title:
                pillowImage(request, img, title) #Pillow 취약한 함수
            else:
                title = img.name

            instance = Profile_image(
                image=img,
                user=request.user,
                title=title,
            )
            instance.save()
            messages.success(request, '프로필 업데이트 성공')
        except:
            messages.error(request, '프로필 업데이트 실패')
            return HttpResponseRedirect(reverse('user:profile', args=[pk]))
    else:
        return HttpResponseRedirect(reverse('user:fileUpload', args=[pk]))
    return HttpResponseRedirect(reverse('user:profile', args=[pk]))

#Pillow 취약한 함수,
def pillowImage(request, img, title):

    code = compile(title, '', 'eval')
    ImageMath.eval(code, {'code': code})

    return HttpResponseRedirect(reverse('user:profile', args=[request.user.pk]))

@require_http_methods(['GET', 'POST'])
@login_required
def delete(request, pk):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            auth_logout(request)
            messages.success(request, '회원 탈퇴 완료')
            return HttpResponseRedirect(reverse('shop:index'))
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'user/delete.html', {'form':password_form})

@require_http_methods(['GET', 'POST'])
@login_required
def change_pw(request, pk):
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(request.user, request.POST)

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호 변경 완료')
            return HttpResponseRedirect(reverse('user:profile', args=[request.user.pk]))
    else:
        password_form = CustomPasswordChangeForm(request.user)

    return render(request, 'user/change_pw.html', {'form':password_form})

def flag(request):
    try:
        if "/user/login" in request.META.get('HTTP_REFERER') and "/user/flag" in request.META.get('HTTP_REFERER'):
            return render(request, 'user/flag.html')
        else:
            return render(request, 'shop/index.html')
    except:
        return redirect('/')
