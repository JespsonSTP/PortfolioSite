from graphene import Field, Mutation, String
from django.contrib.auth import get_user_model
from .types import UserType

User = get_user_model()

'''
I used a multiline string formation for 
#we have to edit the creaate user method for authenthication 

'''

class UserCreate(Mutation):
    user = Field(UserType)

    class Arguments:
        username = String(required=True)
        email = String(required=True)
        password = String(required=True)

    def mutate(self, info, username, password, email):
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return UserCreate(user=user)
