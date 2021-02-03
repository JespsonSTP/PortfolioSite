from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .api.serializers import BlogSerializer, AuthorSerializer, CommentSerializer
from graphene_django.rest_framework.mutation import serializerMutation
from .filters import BlogFilter, AuthorFilter
from .models import Blog, Author, Comment

#urning python objects into node for graphql

class BlogNode(DjangoObjectType):
    class Meta:
        model = Blog
        interfaces = (relay.Node, )


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        interfaces = (relay.Node, )

class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
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

class Query(ObjectType):
    blog = relay.Node.field(BlogNode)
    blogs = DjangoFilterConnectionField(BlogNode, filterset_class=BlogFilter)
    author = relay.Node.field(AuthorNode)
    authors = DjangoFilterConnectionField(AuthorNode, filterset_class=AuthorFilter)


class Mutation(ObjectType):
    blog_mutation = BlogMutation.field()
    author_mutation = AuthorMutation.field()
    comment_mutation = CommentMutation.field()