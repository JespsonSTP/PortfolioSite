from rest_framework import serializers
from djangobackend.models import Blog, Author, Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id',)
        extra_kwargs = {
            'id'; {'read_only':False, 'required':False}
        }

        #edititing the create method because in graphql it wont't
        #allows you to create an author with the blog fue to nested serializations
        def create(self, validated_data):
            author_data = validated_data.pop('author')
            author, created = Author.objects.get_or_create(**author_data)
            blog = blog.objects.create(author=author, **validated_data)
            return blog


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',)
