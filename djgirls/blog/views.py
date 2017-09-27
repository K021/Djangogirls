from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

User = get_user_model()

from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    # posts = Post.objects.all()
    context = {
        # value는 QuerySet
        'posts': posts,
    }

    return render(request, 'blog/post_list.html', context)


# view(controller) 구현
# post_detail 기능을 하는 함수를 구현
# 'post'라는 key로 Post.objects.first()에 해당하는 Post 객체를 전달
#  템플릿은 'blog/post_detail.html'을 사용


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('Post #{} does not exist'.format(pk))
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    if request.method == 'POST' and request.POST.get('title') and request.POST.get('content'):
        p = Post.objects.create(title=request.POST['title'],content=request.POST.get('content'),author=User.objects.get(username='elohimawmar'))
        # p = Post()
        # p.title = request.POST['title']
        # p.content = request.POST['content']
        # p.author = User.objects.get(username='elohimawmar')
        if request.POST.get('publish') == 'on':
            p.publish()
        # else:
        #     p.save()
        return redirect('/')
    elif request.method == 'GET':
        return render(request, 'blog/post_form.html')
    else:
        return redirect('/post/add')


def post_test(request):
    return render(request, 'blog/post_form2.html')