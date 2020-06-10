from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

def create_user():
    User.objects.filter(firstName="Snoopy",lastName="Lee").update(firstName="Emily")