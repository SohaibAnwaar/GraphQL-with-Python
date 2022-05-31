import graphene
from serializers import (
    MyCarGrapheneInputModel,
    MyCarGrapheneModel
)
from models.my_car import MyCar


class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String())

    @staticmethod
    def resolve_say_hello(parent, info, name):
        return f'Hello {name}'

class CreateMyCar(graphene.Mutation):
    class Arguments:
        car_details=MyCarGrapheneInputModel()

    Output=MyCarGrapheneModel

    @staticmethod
    def mutate(parent, info, car_details):
        my_car = MyCar()
        my_car.name = car_details.name
        my_car.save()

        return my_car

class Mutation(graphene.ObjectType):
    create_my_car = CreateMyCar.Field()