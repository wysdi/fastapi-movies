from typing import List, Optional

from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    genre: str
    studio: str
    score: int
    profit: int
    year: str
    gross: str

    class Config:
        orm_mode = True