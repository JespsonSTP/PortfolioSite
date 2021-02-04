import django_filters
from .models import Blog, Author

class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = ('fullname')

class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ('title')
