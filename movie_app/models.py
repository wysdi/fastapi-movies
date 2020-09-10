from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    genre = Column(String(20))
    studio = Column(String(50))
    score = Column(Integer)
    profit = Column(Integer)
    rotten = Column(Integer)
    year = Column(String(10))
    gross = Column(String(100))

