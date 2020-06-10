from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('articles',views.articles, name="articles"),
    path('author',views.author, name="author"),
path('comments',views.comments, name="comments"),
path('create',views.create, name="create"),
]