from pydantic import BaseModel
from typing import Optional

class Serie(BaseModel):

    id: Optional[int]= None
    title:str
    year:int
    genre:str
    seassons:int

    class config:
        orm_mode = True