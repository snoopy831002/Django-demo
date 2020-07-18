from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import get_articles, create_articles
from .form import django_form
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache
#import logging
#logger = logging.getLogger('django')

# Create your views here.
def index(request):
    articles = get_articles()
    content = {"articles":articles}
    return render(request,'index.html',content)

@require_http_methods(['POST'])
def comments(request):
    d_form = django_form(request.POST)
    if d_form.is_valid():
        print ("form is ok!")
    else :
        print("form is bad!")
    # Save comments
    content = request.POST.get('content')
    create_articles(content)
    return HttpResponse("Comments updated!")

def articles(request, a_num):
    #return HttpResponse("this is articles")

    form = django_form()
    if request.user.is_authenticated:
        context = {"form":form,"user":request.user.username}
    else:
        context = {"form":form,"user":""}
    return render(request,"articles.html", context)



def author(request):
    articles = cache.get("root") # key
    if not articles:
        articles = get_articles()
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
        return render(request, "articles.html")
    else:
        return render(request, "login.html")

def snd_mail(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        settings.EMAIL_HOST_USER,
        ['snoopy831002@gmail.com'],
        fail_silently=False,
    )