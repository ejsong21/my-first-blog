# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'kilogram'

urlpatterns = [
    path('kilogram_list', views.kilogram_list, name='kilogram_list'),
]
