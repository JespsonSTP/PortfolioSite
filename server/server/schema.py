from graphene import Schema, ObjectType
import djangobackend.schema

#there a pass because it inherits from the other queries
class Query(djangobackend.schema.Query, ObjectType):
    pass

class Mutation(djangobackend.schema.Mutation, ObjectType):
    pass

schema = Schema(query=Query, mutation=Mutation)