from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, api
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/search")
def search_movies(
    title: str = None,
    year: int = None,
    genre: str = None,
    person: str = None,
    title_type: str = None,
    db: Session = Depends(get_db),
):
    return api.search_movies(db, title, year, genre, person, title_type)
