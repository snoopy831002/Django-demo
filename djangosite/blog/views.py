from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import create_user

# Create your views here.
def index(request):
    return render(request,'author.html')

@require_http_methods(['GET'])
def comments(request):
    # Save comments
    return HttpResponse("Comments updated!")

def articles(request):
    #return HttpResponse("this is articles")
    return render(request,"articles.html")

def author(request):
    return render(request,"author.html")
    #return redirect('articles')

def create(request):
    create_user()
    return HttpResponse("User created")