from typing import List, Optional
from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class MyCarModel(BaseModel):
    id: int
    name: str




class MyCarGrapheneModel(PydanticObjectType):
    class Meta:
        model = MyCarModel

class MyCarGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = MyCarModel