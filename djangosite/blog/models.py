from django.db import models
from django.contrib.auth.models import User as auth_user

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, default='Tech')
    description = models.TextField(max_length=500, default="Tech")
    def __str__(self):
        return self.name

class Articles(models.Model):
    user = models.ForeignKey(auth_user,on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=False, null=False)
    content = models.CharField(max_length=500, blank=False, null=False)
    last_update = models.DateField(auto_now=True)
    tags = models.ManyToManyField(
        Tag,
        related_name='articles_related_tags'
    )

def _create_articles(request):
    a = Articles.objects.create(user = request.user, title = request.POST['title'], content = request.POST['content'])
    query = dict(request.POST)
    for i in query['tags']:
        a.tags.add(Tag.objects.get(id=i))
    return

def _edit_articles_by_id(request,id):
    Articles.objects.filter(id=id).update(title = request.POST['title'], content = request.POST['content']) # No need to update user
    a = Articles.objects.filter(id=id).get()
    a.tags.remove() # Remove all of the previous tags
    query = dict(request.POST)
    for i in query['tags']:
        a.tags.add(Tag.objects.get(id=i)) # Update the new tags
    return

def _get_articles():
    #
    # Get all of the articles
    #
    #
    return Articles.objects.all().order_by('-last_update')

def _get_articles_by_id(id):
    return Articles.objects.filter(id=id).first() # Uses "first()" because Django objects return objects by default

def _del_articles_by_id(id):
    Articles.objects.filter(id=id).delete()
    return
