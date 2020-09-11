from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movies/", response_model=List[schemas.Movie])
def read_movie(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_movies(db, skip=skip, limit=limit)
    return users


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise  HTTPException(status_code=404, detail="Movie not found")

    return db_movie


@app.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=movie.title)
    if db_movie:
        raise HTTPException(status_code=400, detail="Movie already registered")

    return crud.create_movie(db=db, movie=movie)


@app.put("/movies/{movie_id}", response_model=schemas.Movie)
def update_movie(movie_id: int, movie: schemas.MovieOut, db : Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise  HTTPException(status_code=404, detail="Movie not found")

    return crud.update_movie(db=db, id=movie_id, movie=movie)


@app.delete("/movies/{movie_id}", response_model=None)
def delete_movie(movie_id: int, db: Session = Depends((get_db))):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise  HTTPException(status_code=404, detail="Movie not found")

    return crud.delete_movie(db=db, id=movie_id)