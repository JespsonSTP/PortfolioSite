from rest_framework import serializers
from djangobackend.models import Author, Blog, Comment, Project


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only':False, 'required':False}
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

class AuthorSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
