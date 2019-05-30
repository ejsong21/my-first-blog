from django.apps import AppConfig
from django.urls import path
from. import views


class AppConfig(AppConfig):
    name = 'app'
    urlpatterns = [
        path('', views.index, name='index'),
    ]
