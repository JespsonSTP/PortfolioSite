from djangobackend.models import Blog, Author, Comment, Project
from djangobackend.filters import BlogFilter, AuthorFilter
from .serializers import BlogSerializer, AuthorSerializer, CommentSerializer, ProjectSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


#it comes with crud already included 
#that's why we uses viewswt instead of apiview cause3 apiview is where you build
#crud operation but viewset all to do more filtering

class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    filterset_class = BlogFilter

class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    filterset_class = AuthorFilter

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=AuthorSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer


