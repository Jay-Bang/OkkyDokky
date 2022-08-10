from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'okkydokky'

urlpatterns = [
    path('home/', views.homeView, name='home'),
    path('board/', views.boardView, name='board'),
    path('mypage/<int:user>/', views.mypageView, name='mypage'),
    path('scrap/<int:pk>/', views.scrapPost, name='scrappost'),
    path('delete/<int:pk>/', views.deletePost, name='deletepost'),

    path('login/', views.logIn, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('signup/', views.signUp, name='signup'),
    path('delete/', views.deleteAccount, name='delete'),
]