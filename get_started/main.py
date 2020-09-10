from typing import Optional
from fastapi import FastAPI

import json

app = FastAPI()

#using External Local Data
with open("./get_started/movie.json") as f:
    movies = json.load(f)


@app.get('/api/v1/movies')
async def get_movies():
    return {"movies": movies}


@app.get('/api/v1/movie/{title}')
async def get_movie(title):
    movie = [movie for movie in movies if movie['Film'] == title]
    return {"movie": movie}

