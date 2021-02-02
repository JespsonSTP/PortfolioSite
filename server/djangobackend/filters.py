import django_filters
from .models import Blog, Author

class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ('title')

class AuthorFilter(django_filters.FilterSet):
    fullname = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Author
        fields = ('fullname')