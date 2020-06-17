from django.db import models
from django.contrib.auth.models import User as auth_user
import uuid

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Articles(models.Model):
    user = models.ForeignKey(auth_user,on_delete=models.CASCADE)
    content = models.CharField(max_length=500, blank=False, null=False)
    last_update = models.DateField(auto_now=True)

def create_user():
    User.objects.filter(firstName="Snoopy",lastName="Lee").update(firstName="Emily")

def create_articles(content):
    user = auth_user.objects.get(username="root")
    Articles.objects.create(user= user, content=content)
    return


def get_articles():
    user = auth_user.objects.get(username="root")
    return Articles.objects.filter(user = user).all().order_by("-last_update")


#def get_article_owner():
    #article = Articles.objects.get(id=2)
    #user = article.user

    #user = Articles.objects.get(id=2).select_related('user')