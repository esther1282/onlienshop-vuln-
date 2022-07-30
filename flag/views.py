from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Flag, User_total

def index(request):
    try:
        Total = User_total.objects.get(user=request.user)
    except User_total.DoesNotExist:
        Total = User_total.objects.create(user=request.user)
        Total.save()

    if request.method == "POST":
        input = request.POST['flag']
        flag = Flag.objects.create(user=request.user, data=input)

        if flag.check_flag:
            messages.success(request, '정답입니다!!')
            Total.add_total
            Total.save()
            messages.success(request, Total.get_total)
        else:
            flag.delete()
            messages.error(request, 'FLAG가 올바르지 않습니다.')

        return HttpResponseRedirect(reverse('flag:index'))
    else:
        return render(request, 'flag/index.html')


