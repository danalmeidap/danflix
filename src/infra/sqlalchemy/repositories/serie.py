from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from typing import List

class SerieRepository:

    def __init__(self, db:Session) -> None:
        self.__db = db

    def create(self, serie:schemas.Serie)->models.Serie:
        db_serie:models.Serie = models.Serie(title = serie.title,
                                year= serie.year,
                                genre= serie.genre,
                                seassons= serie.seassons)
        self.__db.add(db_serie)
        self.__db.commit()
        self.__db.refresh(db_serie)
        return db_serie

    def series_list(self) ->List[models.Serie]:
        return self.__db.query(models.Serie).all()

    def get_serie(self, serie_id:int) ->models.Serie:
        return self.__db.query(models.Serie).get(serie_id)

    def update(self, serie_id:int, serie:schemas.Serie)->models.Serie:
        db_serie: models.Serie = self.get_serie(serie_id)
        db_serie.title = serie.title
        db_serie.year = serie.year  
        db_serie.genre = serie.genre
        db_serie.seassons = serie.seassons
        self.__db.commit()
        self.__db.refresh(db_serie)
        return db_serie


    def remove(self, serie_id) ->bool:
        db_serie = self.get_serie(serie_id)
        if db_serie:
            self.__db.delete(db_serie)
            self.__db.commit()
            return True
        return False
        
            

