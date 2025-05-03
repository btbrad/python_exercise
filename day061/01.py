from graphene import ObjectType, Schema, String

class Query(ObjectType):
    say = String()

    def resolve_say(self, info):
        return 'Hello GraphQL!'
    

if __name__ == '__main__':
    schema = Schema(query= Query)
    query_string = """
    {
        say
    }
    """
    rs = schema.execute(query_string)
    print(rs.data)
    
