from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('articles/<int:a_num>',views.articles, name="articles"),
    path('author',views.author, name="author"),
    path('comments',views.comments, name="comments"), #backends function
    path('signin',views.login, name="login"),
    path('login',views.usr_login, name="usr_login"), #backends function
]