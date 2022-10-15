from fastapi import FastAPI
import typing
import strawberry
from strawberry.asgi import GraphQL
from enum import Enum

@strawberry.type
class Person:
    email: str
    name: str
    address: 'Address'
    age: int

def get_People():
    return [
        Person( 
            name = "Kevin Rudd",
            email= "krudd@gmail.com", 
            address = Address(
                number = 1,
                street = "Hue Hue Rd",
                city = "Canberra",
                state = State.NSW
            ),
            age = 60
        ),
        Person( 
            name = "Malcom Turnbull",
            email= "mturnbull@gmail.com", 
            address = Address(
                number = 2,
                street = "Starling Crs",
                city = "Perth",
                state = State.WA
            ),
            age = 1000
        ),
        Person( 
            name = "Tony Abbot",
            email= "tabbot@gmail.com", 
            address = Address(
                number = 3,
                street = "Libral Ln",
                city = "Darwin",
                state = State.NT
            ),
            age = 1000
        ),
    ]

@strawberry.type
class Address:
    number: int
    street: str
    city: str
    state: 'State'

@strawberry.enum
class State(Enum):
    NSW = "NSW"
    WA = "WA"
    NT = "NT"
    SA = "SA"
    QLD = "QLD"
    VIC = "VIC"
    ACT = "ACT"
    TAS = "TAS"

@strawberry.type
class Query:
    person: typing.List[Person] = strawberry.field(resolver=get_People)

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)


@app.get("/")
async def root():
    return {"message": "Hello World"}