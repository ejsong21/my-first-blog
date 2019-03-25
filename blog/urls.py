# -*- coding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
        # WARNING:django.request:Not Found: /favicon.ico를 피하기 위해
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),

]