from typing import List, Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    genre: str
    studio: str


class MovieOut(MovieBase):
    score: Optional[int] = None
    profit: Optional[int] = None
    rotten: Optional[int] = None
    year: Optional[str] = None
    gross: Optional[str] = None


class Movie(MovieOut):
    id: int

    class Config:
        orm_mode = True
