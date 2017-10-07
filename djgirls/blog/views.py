from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Post

User = get_user_model()


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


def post_detail(request, pk, ask_delete=None):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('Post #{} does not exist'.format(pk))
    if ask_delete:
        context = {
            'post': post,
            'delete': True,
        }
        return render(request, 'blog/post_detail.html', context)
    context = {
        'post': post,
        'delete': False,
    }
    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    if request.method == 'POST' and request.POST.get('title') and request.POST.get('content'):
        p = Post.objects.create(
            title=request.POST['title'],
            content=request.POST.get('content'),
            author=User.objects.get(username='elohimawmar')
        )
        # p = Post()
        # p.title = request.POST['title']
        # p.content = request.POST['content']
        # p.author = User.objects.get(username='elohimawmar')
        if request.POST.get('publish') == 'on':
            p.publish()
        # else:
        #     p.save()
        return redirect('post_detail', pk=p.pk)
    elif request.method == 'GET':
        context = {
            'content': True,
        }
        return render(request, 'blog/post_form.html', context)
    else:
        context = {
            'content': False,
        }
        return render(request, 'blog/post_form.html', context)


def post_delete(request, pk, delete_request=None):
    if delete_request:
        context = {
            'delete': True,
        }
        return render(request, 'blog/post_detail.html', context)
    elif request.method == 'POST':
        p = Post.objects.get(pk=pk)
        p.delete()
        return redirect('/')
    return HttpResponse('Permission denied', status=403)


def post_test(request):
    return render(request, 'blog/post_form2.html')