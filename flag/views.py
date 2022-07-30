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

    Score_set = User_total.objects.order_by('-total')

    if request.method == "POST":
        input = request.POST['flag']
        flag = Flag.objects.create(user=request.user, data=input)

        if flag.check_flag:
            flag_set = Flag.objects.filter(user=request.user).order_by('date_ordered')
            for i in range(0, len(flag_set) - 1):
                if flag.data == flag_set[i].data:
                    messages.error(request, '이미 제출한 flag입니다.')
                    flag.delete()
                    return HttpResponseRedirect(reverse('flag:index'))
            messages.success(request, '정답입니다!!')
            Total.add_total
            Total.save()
            messages.success(request, str(Total.get_total)+'점 획득!!')
        else:
            flag.delete()
            messages.error(request, 'FLAG가 올바르지 않습니다.')

        return HttpResponseRedirect(reverse('flag:index'))
    else:
        return render(request, 'flag/index.html', {'myscore':Total.get_total, 'score_set':Score_set, 'num':0})
