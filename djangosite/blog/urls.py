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
path('sign',views.login, name="login"),
path('login',views.usr_login, name="login"),
path('cookies',views.cookies, name="cookies"),
path('get_cookies',views.get_cookies, name="get_cookies"),
path('set_session',views.set_session, name="set_session"),
path('get_session',views.get_session, name="get_session"),
path('send_mail',views.snd_mail, name="send_mail"),
]