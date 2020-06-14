from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('articles/<int:a_num>',views.articles, name="articles"),
    path('author',views.author, name="author"),
    path('comments',views.comments, name="comments"),
    path('create',views.create, name="create"),
    path('upload',views.upload_file, name="upload"),
    path('download',views.download_file, name="download"),
]