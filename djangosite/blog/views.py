from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import create_articles
from .form import django_form
from .upload import UploadFileForm
import os

# Create your views here.
def index(request):
    return render(request,'author.html')

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
    context = {"form":form}
    #print (a_num)
    return render(request,"articles.html", context)

def author(request):
    context = {
        "name" : "Snoopy",
        "sidebar" : ["Home","Articles","Authors"]
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