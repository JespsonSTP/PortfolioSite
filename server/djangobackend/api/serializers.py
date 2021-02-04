from rest_framework import serializers
from djangobackend.models import Blog, Author, Comment, Project


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id',)

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id',)
        extra_kwargs = {
            'id'; {'read_only':False, 'required':False}
        }

        #edititing the create method because in graphql it wont't
        #allows you to create an author with the blog due to nested serializations
        def create(self, validated_data):
            author_data = validated_data.pop('author')
            author, created = Author.objects.get_or_create(**author_data)
            blog = blog.objects.create(author=author, **validated_data)
            return blog
        
        def update(self, instance, validated_data):
            author_data = validated_data.pop('author')
            author, created = Author.objects.get_or_create(**author_data)
            instance.author = author
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
            return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id',)
