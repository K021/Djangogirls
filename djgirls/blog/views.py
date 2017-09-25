from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        # value는 QuerySet
        'posts': posts,
    }

    return render(request, 'blog/post_list.html', context)
