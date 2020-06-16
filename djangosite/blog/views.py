from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import get_articles
from .form import django_form
from .upload import UploadFileForm
from .login import login_form
import os
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import logging
logger = logging.getLogger('django')

def set_session(request):
    request.session['pref'] = "C++"
    response = HttpResponse("Session set!")
    return  response

def get_session(request):
    response = HttpResponse("Session set!"+str(request.session['pref']))
    return  response

def get_cookies(request):
    if "pref" in request.COOKIES:
        print("pref:",request.COOKIES['pref'])

def cookies(request):
    response = HttpResponse("Cookie set!")
    response.set_cookie("pref","PYTHON")
    return response

# Create your views here.
def index(request):
    return render(request,'index.html',{"form":login_form})

@require_http_methods(['POST'])
def comments(request):

    d_form = django_form(request.POST)
    if d_form.is_valid():
        print ("form is ok!")
    else :
        print("form is bad!")
    #request.schem
    #return HttpResponse("Fucked")
    # Save comments
    #content = request.POST.get('content')
    #create_articles(content)
    #return HttpResponse("Comments updated!")
    context = {"form":d_form}
    #print (a_num)
    return render(request,"articles.html", context)

def articles(request, a_num):
    #return HttpResponse("this is articles")

    form = django_form()
    if request.user.is_authenticated:
        context = {"form":form,"user":request.user.username}
    else:
        context = {"form":form,"user":""}
    #print (a_num)
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
    #return redirect('articles')

def create(request):
    create_user()
    return HttpResponse("User created")

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("form valid")
            with open('/Users/zhonghaoli/upload.txt','wb+') as destination:
                for chunk in request.FILES['file']:
                    destination.write(chunk)
                return HttpResponse("File updated")
        else:
            print("form invalid")
    else:
        form = UploadFileForm()
        return  render(request,"upload.html", {"form":form})

def download_file(request):
    file_path = os.path.join("/Users/zhonghaoli/","../../manage.py".strip('../').strip("./").strip("/"))
    response = HttpResponse(open(file_path,'rb'),content_type="application/zip")
    response['Content-Disposition'] = 'attachment; filename="{}"'.format("download")
    return response

def usr_login(request):
    user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
    if user is not None:
        login(request, user)
        return HttpResponse("LOGIN SUCCESSFUL =)")

    else:
        return HttpResponse("LOGIN FAILED QAQ")


def snd_mail(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        settings.EMAIL_HOST_USER,
        ['snoopy831002@gmail.com'],
        fail_silently=False,
    )