from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from user.models import User
from .forms import WriteForm
from django.core.paginator import Paginator

def index(request):
    if request.method =='GET':
        param = request.GET.get("param", "")
        nonce = "12345"
        return render(request, "board/index.html", {"param": param, "nonce": nonce})
    else:
        return render("index.html")

def list(request):
    post_list = Post.objects.order_by('-date')

    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 10) # 한페이지당 개수
    post_page = paginator.get_page(page)

    return render(request, 'board/list.html', {'posts': post_page, 'user': request.user})

def write(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('/user/login')

    if request.method == 'GET':
        write_form = WriteForm()
        return render(request, 'board/write.html', {'forms': write_form})

    elif request.method == 'POST':
        write_form = WriteForm(request.POST)

        if write_form.is_valid():
            # writer = User
            post = Post(
                title = write_form.title,
                content = write_form.content,
                writer = request.user,
                is_secret = write_form.is_secret
            )
            post.save()
            return redirect('/board')
        else:
            context = {'forms': write_form}
            if write_form.errors:
                for value in write_form.erros.values():
                    context['error'] = value
            return render(request, 'board/write.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'board/detail.html', {'post': post})

def modify(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        write_form = WriteForm(instance=post)
        return render(request, 'board/modify.html', {'forms': write_form})

    elif request.method == 'POST':
        write_form = WriteForm(request.POST)

        if write_form.is_valid():
            post.title = write_form.title
            post.content = write_form.content
            post.is_secret = write_form.is_secret
            post.save()
            return redirect('/board')
        else:
            context = {'forms': write_form}
            if write_form.errors:
                for value in write_form.erros.values():
                    context['error'] = value
            return render(request, 'board/modify.html', context)


def delete(request, post_id):
    # 본인인지 확인하는 login
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('/board')
