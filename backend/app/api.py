from sqlalchemy.orm import Session
from sqlalchemy import and_
from . import models


def search_movies(
    db: Session,
    title: str = None,
    year: int = None,
    genre: str = None,
    person: str = None,
    title_type: str = None,
):
    query = db.query(models.Title)

    if title:
        query = query.filter(models.Title.primary_title.ilike(f"%{title}%"))

    if year:
        query = query.filter(models.Title.start_year == year)

    if genre:
        query = query.join(models.Title.genres).filter(
            models.Genre.name.ilike(f"%{genre}%")
        )

    if person:
        query = query.join(models.Title.people).filter(
            models.Person.primary_name.ilike(f"%{person}%")
        )

    if title_type:
        query = query.filter(models.Title.title_type.ilike(f"%{title_type}%"))

    results = query.all()

    return [
        {
            "Title": title.primary_title,
            "Year Released": title.start_year,
            "Type": title.title_type,
            "Genre": [genre.name for genre in title.genres],
            "List of People Associated with the title": [
                person.primary_name for person in title.people
            ],
        }
        for title in results
    ]
