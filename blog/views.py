# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
# post_list라는 함수(def) 만들어 요청(request)을 넘겨받아
# render메서드를 호출한다.
# 이 함수는 호출하여 받은 (return) blog/post_list.html 템플릿을 보여준다.

#render 함수에는 매개변수 request 와 blog/post_list.html 템플릿이 있다.
# {} 이곳에 템플릿을 사용하기 위해 매개변수를 추가할 것이다.
# {'posts': posts} 이렇게.. : 이전에 문자열이 와야하고, 작은따옴표를 양쪽에 붙여야 한다.

def post_list(request):
    #posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list2.html', {'posts':posts})
    
    
