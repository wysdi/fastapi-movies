from sqlalchemy.orm import Session

from . import schemas, models


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()


