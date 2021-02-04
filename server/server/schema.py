from graphene import Schema, ObjectType
import djangobackend.schema
import users.gql.schema


#there a pass because it inherits from the other queries
class Query(djangobackend.schema.Query, users.gql.schema.Query, ObjectType):
    pass

class Mutation(djangobackend.schema.Mutation, users.gql.schema.Mutation, ObjectType):
    pass

schema = Schema(query=Query, mutation=Mutation)