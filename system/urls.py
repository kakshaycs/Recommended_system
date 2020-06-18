from django.urls import path
from . import views

urlpatterns = [
    path('',views.Choose, name='choose'),
    path('user',views.User, name='user'),
    path('song',views.Song, name = 'song'),
]