from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


def post_list(request):
    # posts = Post.objects.filter(published_date__isnull=False)
    posts = Post.objects.all()
    context = {
        # value는 QuerySet
        'posts': posts,
    }

    return render(request, 'blog/post_list.html', context)

# view(controller) 구현
# post_detail 기능을 하는 함수를 구현
# 'post'라는 key로 Post.objects.first()에 해당하는 Post 객체를 전달
#  템플릿은 'blog/post_detail.html'을 사용


def post_detail(request):
    post = Post.objects.first()
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)