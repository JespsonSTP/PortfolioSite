from djangobackend.models import Blog, Author
from .serializers import BlogSerializer, AuthorSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


#it comes with crud already included 
#that's why we uses viewswt instead of apiview cause3 apiview is where you build
#crud operation but viewset all to do more filtering

class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

