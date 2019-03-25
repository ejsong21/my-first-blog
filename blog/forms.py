# -*- coding: utf-8 -*-
from django import forms
from .models import Post

# form이름은 PostForm이다. 그리고 이 폼은 ModelForm이다.
class PostForm(forms.ModelForm):
    # 이 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 django에게 알려준다.
    # 일단 이번에는 fields에 title과 text만 넣음.
    class Meta:
        model = Post
        fields = ('title', 'text',)
        