from pydantic import BaseModel
from typing import Optional

class Serie(BaseModel):
    
    id:Optional[int]= None
    title:str
    genre:str
    seassons:str

    class Config:
        orm_mode = True
