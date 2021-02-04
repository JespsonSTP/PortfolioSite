from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .api.serializers import BlogSerializer, AuthorSerializer, CommentSerializer, ProjectSerializer
from graphene_django.rest_framework.mutation import serializerMutation
from .filters import BlogFilter, AuthorFilter
from .models import Blog, Author, Comment, Project

#urning python objects into node for graphql

class BlogNode(DjangoObjectType):
    class Meta:
        model = Blog
        interfaces = (relay.Node, )


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = {
            'fullname': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )

class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
        interfaces = (relay.Node, )

class ProjectNode(DjangoObjectType):
    class Meta:
        model = Project
        interfaces = (relay.Node, )

class BlogMutation(serializerMutation):
    class Meta:
        serializer_class = BlogSerializer

class AuthorMutation(serializerMutation):
    class Meta:
        serializer_class = AuthorSerializer

class CommentMutation(serializerMutation):
    class Meta:
        serializer_class = CommentSerializer

class ProjectMutation(serializerMutation):
    class Meta:
        serializer_class = ProjectSerializer

class Query(ObjectType):
    blog = relay.Node.field(BlogNode)
    blogs = DjangoFilterConnectionField(BlogNode, filterset_class=BlogFilter)
    author = relay.Node.field(AuthorNode)
    authors = DjangoFilterConnectionField(AuthorNode, filterset_class=AuthorFilter)
    comment = relay.Node.field(CommentNode)
    comments = DjangoFilterConnectionField(CommentNode)
    project= relay.Node.field(ProjectNode)
    projects = DjangoFilterConnectionField(ProjectNode)


class Mutation(ObjectType):
    blog_mutation = BlogMutation.field()
    author_mutation = AuthorMutation.field()
    comment_mutation = CommentMutation.field()
    project_mutation = projectMutation.field()