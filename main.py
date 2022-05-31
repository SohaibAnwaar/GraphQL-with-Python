import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from schema import Query, Mutation


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)