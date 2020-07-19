from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    #path('articles/<int:a_num>',views.articles, name="articles"),
    path('author',views.author, name="author"),
    path('signin',views.login, name="login"),
    path('create_article',views.create_article, name="create_article"),
    path('login',views.usr_login, name="usr_login"), #backends function
    path('logout',views.usr_logout, name="usr_logout"), #backends function
]