from django.shortcuts import render, redirect
from .models import _get_articles, _create_articles
from .create_articles import create_articles_form, edit_articles_form
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

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
        form = create_articles_form()
        context = {"form":form,"user":""}
        return render(request,"create_articles.html",context)

def edit_article(request,id):
    content = {}
    form = edit_articles_form(id)
    context = {"form":form,"content": content}
    return render(request,"create_articles.html",context)

def author(request):
    context = {
        "name" : "Snoopy",
        "sidebar" : ["Home","Articles","Authors"],
        "articles": articles
    }
    return render(request,"author.html", context)

def login(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
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