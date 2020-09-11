from sqlalchemy.orm import Session

from . import schemas, models


def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()


def get_movie_by_title(db: Session, title: str):
    return db.query(models.Movie).filter(models.Movie.title == title).first()


def create_movie(db: Session, movie: schemas.MovieBase):
    db_movie = models.Movie(title=movie.title, genre=movie.genre, studio=movie.studio )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def update_movie(db: Session, id: int, movie: schemas.MovieOut):
    db.query(models.Movie).filter(models.Movie.id == id).update(movie)
    db.commit()
    return db.query(models.Movie).filter(models.Movie.id == id).first()


def delete_movie(db: Session, id: int):
    db.query(models.Movie).filter(models.Movie.id == id).delete()
    db.commit()
    return None