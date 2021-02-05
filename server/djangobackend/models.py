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

    class META:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


    def __str__(self): 
        return self.fullname
    

class Blog(models.Model):
    title = models.CharField(max_length=50)
    blogpic = models.ImageField(null=True)
    blogpicTwo = models.ImageField(null=True)
    blogpicThree = models.ImageField(null=True)
    blogpicFour = models.ImageField(null=True)
    blogpicFive = models.ImageField(null=True)
    body = models.TextField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='date posted') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date updated') 
    blog_author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)


    #META of blog
    #we use reverse ordering so we can get the newest blogs
    class META:
        ordering = ['-id']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


    def __str__(self): 
        return self.title
    

class Comment(models.Model):
    name = models.CharField(max_length=50)
    Comment = models.TextField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='date posted') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date updated')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    class META:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


    def __str__(self): 
        return self.name

class Project(models.Model):
    projectname = models.CharField(max_length=50)
    videoDescriptionURL = models.CharField(max_length=500)
    textDescription = models.TextField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='date posted') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date updated')

    class META:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


    def __str__(self): 
        return self.projectname

