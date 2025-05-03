from flask import Flask
import graphene
from flask_graphql import GraphQLView

class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_Hello(self):
        return 'Hello Flask GraphQL'

app = Flask(__name__)

if __name__ == '__main__':
    schema = graphene.Schema(query=Query)
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True ))
    app.run(debug=True)