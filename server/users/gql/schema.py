from graphene import Field, List, ObjectType, Schema
from graphql_jwt.decorators import login_required
from graphql_jwt import ObtainJSONWebToken, Verify, Refresh 
from .types import UserType
from .mutations import UserCreate
from django.contrib.auth import get_user_model

User = get_user_model()

class Query(ObjectType):
    current_user = Field(UserType)
    users = List(UserType)

    def resolve_users(root, info):
        return User.objects.all()
    
    @login_required
    def resolve_current_user(root, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in User!')
        return user

class Mutation(ObjectType):
    user_create = UserCreate.Field()
    token_auth = ObtainJSONWebToken.Field()
    Verify_token = Verify.Field()
    Refresh_token = Verify.Field()


schema = Schema(query=Query, mutation=Mutation)