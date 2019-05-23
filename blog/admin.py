# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post, Comment

# Post모델을 등록함
admin.site.register(Post)

# 관리자 패널을 모델에 등록함
admin.site.register(Comment)
