from src.infra.sqlalchemy.config.database import Base
from sqlalchemy import Column, Integer,String

class Serie(Base):
    
    __tablename__ = "serie"

    id= Column(Integer, primary_key= True, index=True)
    title= Column(String)
    year= Column(Integer)
    genre= Column(Integer)
    seassons= Column(Integer)
