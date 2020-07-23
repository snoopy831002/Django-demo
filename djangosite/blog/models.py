from django.db import models
from django.contrib.auth.models import User as auth_user

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
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

def _create_user():
    User.objects.filter(firstName="Snoopy",lastName="Lee").update(firstName="Emily")

def _create_articles(request):
    a = Articles.objects.create(user = request.user, title = request.POST['title'], content = request.POST['content'])
    query = dict(request.POST)
    for i in query['tags']:
        a.tags.add(Tag.objects.get(id=i))
    return

def _get_articles():
    #
    # You should get all articles
    # not articles posted only by root
    #
    #
    user = auth_user.objects.get(username="root")
    return Articles.objects.filter(user = user).all()

def _get_articles_by_id(id):
    print(Articles.objects.filter(id=id).values())
    return Articles.objects.filter(id=id)
