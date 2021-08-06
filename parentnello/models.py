from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    nsfw = models.BooleanField(default=False,blank=True)
    creation_date = models.DateField(auto_now=True)
    rating = models.IntegerField()
    author=models.CharField(max_length=300)
    #comments
    #content

class Comment(models.Model):
    author= models.CharField(max_length=300)
    comment=models.TextField()

class Content(models.Model):
    text=models.TextField(editable=True,blank=True)
    image=models.ImageField(editable=True,blank=True)