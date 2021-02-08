import django_filters
from .models import Blog, Comment, Project

class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ['title']

class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = ['blog']

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['projectname']
