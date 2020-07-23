from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import _get_articles, _create_articles, _get_articles_by_id
from .create_articles import create_articles_form
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache

# Create your views here.
def index(request):
    articles = _get_articles()
    content = {"articles":articles}
    return render(request,'index.html',content)

def create_article(request):
    if request.method == 'POST':
        _create_articles(request)
        return redirect("create_article")
    else:
        context = {"form":create_articles_form,"user":""}
        return render(request,"create_articles.html",context)

def edit_article(request,id):
    content = _get_articles_by_id(id)
    context = {"form":create_articles_form,"content": content}
    #print(content['title'])
    return render(request,"create_articles.html",context)

def author(request):
    articles = cache.get("root") # key
    if not articles:
        articles = _get_articles()
        cache.set("root",articles, 30)

    context = {
        "name" : "Snoopy",
        "sidebar" : ["Home","Articles","Authors"],
        "articles": articles
    }
    return render(request,"author.html", context)

def login(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    #return render(request, "articles.html")
    return redirect("index")

def usr_login(request):
    user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
    if user is not None:
        auth_login(request,user)
        return redirect('index')
    else:
        return redirect('usr_login')

def usr_logout(request):
    auth_logout(request)
    return redirect('index')


def snd_mail(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        settings.EMAIL_HOST_USER,
        ['snoopy831002@gmail.com'],
        fail_silently=False,
    )