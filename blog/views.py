# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
# post_list라는 함수(def) 만들어 요청(request)을 넘겨받아
# render메서드를 호출한다.
# 이 함수는 호출하여 받은 (return) blog/post_list.html 템플릿을 보여준다.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    
