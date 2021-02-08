import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from .api.serializers import BlogSerializer, AuthorSerializer, CommentSerializer, ProjectSerializer
from .filters import BlogFilter, CommentFilter, ProjectFilter
from .models import Author, Blog, Comment, Project

#urning python objects into node for graphql

class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = {
            'fullname': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )

class BlogNode(DjangoObjectType):
    class Meta:
        model = Blog
        interfaces = (relay.Node, )

class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
        interfaces = (relay.Node, )

class ProjectNode(DjangoObjectType):
    class Meta:
        model = Project
        interfaces = (relay.Node, )

    
class AuthorMutation(SerializerMutation):
    class Meta:
        serializer_class = AuthorSerializer

class BlogMutation(SerializerMutation):
    class Meta:
        serializer_class = BlogSerializer

class CommentMutation(SerializerMutation):
    class Meta:
        serializer_class = CommentSerializer

class ProjectMutation(SerializerMutation):
    class Meta:
        serializer_class = ProjectSerializer

class Query(ObjectType):
    author = relay.Node.Field(AuthorNode)
    authors = DjangoFilterConnectionField(AuthorNode)
    blog = relay.Node.Field(BlogNode)
    blogs = DjangoFilterConnectionField(BlogNode, filterset_class=BlogFilter)
    comment = relay.Node.Field(CommentNode)
    comments = DjangoFilterConnectionField(CommentNode,  filterset_class= CommentFilter)
    project= relay.Node.Field(ProjectNode)
    projects = DjangoFilterConnectionField(ProjectNode, filterset_class= ProjectFilter)


class Mutation(ObjectType):
    author_mutation = AuthorMutation.Field()
    blog_mutation = BlogMutation.Field()
    comment_mutation = CommentMutation.Field()
    project_mutation = ProjectMutation.Field()