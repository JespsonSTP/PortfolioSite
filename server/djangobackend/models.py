from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=500)
    avatar = models.ImageField(null=True)
    aboutme = models.TextField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='date posted') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date updated') 
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='owner'
    )
    #slug = models.SlugField(blank=True, unique=True)

    def __str__(self): 
        return self.fullname
    

class Blog(models.Model):
    title = models.CharField(max_length=50)
    blogpic = models.ImageField(null=True)
    body = models.TextField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='date posted') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date updated') 
    blog_author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self): 
        return self.title
    

    
