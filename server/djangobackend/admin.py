from django.contrib import admin
from djangobackend.models import Author, Blog, Comment, Project

# Register your models here.

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Project)