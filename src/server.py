from fastapi import Depends, FastAPI, Response, status
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import create_db, get_db
from src.infra.sqlalchemy.repositories.serie import SeriesRepository
from src.schemas.schemas import Serie

app = FastAPI()
create_db()


@app.get("/series")
async def series_list(response: Response, db: Session = Depends(get_db)):
    return SeriesRepository(db).series_list()


@app.get("/series/{serie_id}")
async def get_serie_by_id(
    serie_id: int, response: Response, db: Session = Depends(get_db)
):
    serie = SeriesRepository(db).get_serie(serie_id)
    if not serie:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:    
        response.status_code = status.HTTP_200_OK
    return serie if serie else response


@app.post("/series")
async def create_serie(
    serie: Serie, response: Response, db: Serie = Depends(get_db)
):
    created_serie = SeriesRepository(db).create(serie)
    response.status_code = status.HTTP_200_OK    
    return created_serie


@app.put("/series/{serie_id}")
async def update_serie(
    serie_id, response: Response, serie: Serie, db: Session = Depends(get_db)
):
    db_serie = SeriesRepository(db).get_serie(serie_id)
    if not db_serie:
        response.status_code = status.HTTP_404_NOT_FOUND 
    if db_serie:
        response.status_code = status.HTTP_200_OK
        updated_serie = SeriesRepository(db).update(serie_id, serie)    
        return updated_serie if updated_serie else response


@app.delete("/series/{serie_id}")
async def delete_serie(
    serie_id: int, response: Response, db: Session = Depends(get_db)
):
    serie = SeriesRepository(db).get_serie(serie_id)
    if not serie:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        if SeriesRepository(db).remove(serie_id):
            response.status_code = status.HTTP_200_OK
            return (
                f"Serie {serie.title} was deleted"
                if response.status_code == status.HTTP_200_OK
                else response
            )