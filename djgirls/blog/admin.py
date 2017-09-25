from django.contrib import admin
from .models import Post
# 같은 패키지 안의 models를 의미한다 from blog.models와 같다

admin.site.register(Post)
