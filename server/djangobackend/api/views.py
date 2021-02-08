from djangobackend.models import Author, Blog, Comment, Project
from djangobackend.filters import BlogFilter, CommentFilter, ProjectFilter
from .serializers import AuthorSerializer, BlogSerializer, CommentSerializer, ProjectSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


#it comes with crud already included 
#that's why we uses viewswt instead of apiview cause3 apiview is where you build
#crud operation but viewset all to do more filtering

class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    filterset_class = BlogFilter

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=AuthorSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer


