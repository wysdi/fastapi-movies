import json

from movie_app import models
from movie_app.database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)
with open("../get_started/movie.json") as f:
    movies = json.load(f)

    for row in movies:
        db_record = models.Movie(
            title=row["Film"],
            genre=row["Genre"],
            studio=row["Lead Studio"],
            score=row["Audience score %"],
            profit=row["Profitability"],
            year=row["Year"],
            rotten=row["Rotten Tomatoes %"],
            gross=row["Worldwide Gross"]
        )
        db.add(db_record)

    db.commit()

db.close()
