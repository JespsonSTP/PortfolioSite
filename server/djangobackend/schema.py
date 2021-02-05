from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .api.serializers import BlogSerializer, AuthorSerializer, CommentSerializer, ProjectSerializer
from graphene_django.rest_framework.mutation import serializerMutation
from .filters import BlogFilter, AuthorFilter
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

    
class AuthorMutation(serializerMutation):
    class Meta:
        serializer_class = AuthorSerializer

class BlogMutation(serializerMutation):
    class Meta:
        serializer_class = BlogSerializer

class CommentMutation(serializerMutation):
    class Meta:
        serializer_class = CommentSerializer

class ProjectMutation(serializerMutation):
    class Meta:
        serializer_class = ProjectSerializer

class Query(ObjectType):
    author = relay.Node.field(AuthorNode)
    authors = DjangoFilterConnectionField(AuthorNode, filterset_class=AuthorFilter)
    blog = relay.Node.field(BlogNode)
    blogs = DjangoFilterConnectionField(BlogNode, filterset_class=BlogFilter)
    comment = relay.Node.field(CommentNode)
    comments = DjangoFilterConnectionField(CommentNode)
    project= relay.Node.field(ProjectNode)
    projects = DjangoFilterConnectionField(ProjectNode)


class Mutation(ObjectType):
    author_mutation = AuthorMutation.field()
    blog_mutation = BlogMutation.field()
    comment_mutation = CommentMutation.field()
    project_mutation = projectMutation.field()