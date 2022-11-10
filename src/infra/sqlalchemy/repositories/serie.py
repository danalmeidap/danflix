from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class SeriesRepository:

    def __init__(self, db:Session) -> None:
        self.__db = db

    def create(self, serie: schemas.Serie) ->models.Serie:
        db_serie = models.Serie(title = serie.title,
                    year= serie.year,
                    genre= serie.genre,
                    seassons= serie.seassons)
        self.__db.add(db_serie)
        self.__db.commit()
        self.__db.refresh(db_serie)
        return db_serie

    def series_list(self) ->List[models.Serie]:
        series= self.__db.query(models.Serie).all()
        return series

    def get_serie(self, serie_id:int) ->models.Serie:
        db_serie = self.__db.query(models.Serie).get(serie_id)
        return db_serie

    def update(self, serie_id:int, serie:schemas.Serie) ->models.Serie:
        db_serie:models.Serie= self.__db.query(models.Serie).get(serie_id)
        db_serie.title = serie.title
        db_serie.year = serie.year
        db_serie.genre = serie.genre
        db_serie.seassons = serie.seassons
        self.__db.commit()
        self.__db.refresh(db_serie)
        return db_serie     

    def remove(self, serie_id:int) ->bool:
        db_serie:models.Serie= self.__db.query(models.Serie).get(serie_id)
        if db_serie:
            self.__db.delete(db_serie)
            self.__db.commit()
            return True
        return False

    def get_by_name(self, serie_name:str) ->models.Serie:
        db_serie = self.__db.execute(statement=select(models.Serie).where(models.Serie.title==serie_name.lower()))
        return db_serie   