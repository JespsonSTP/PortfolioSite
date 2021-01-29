from rest_framework import serializers
from djangobackend.models import Blog, Author

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id',)
