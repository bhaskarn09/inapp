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


def search_people(
    db: Session,
    name: str = None,
    profession: str = None,
    movie: str = None,
):
    query = db.query(models.Person)

    if name:
        query = query.filter(models.Person.primary_name.ilike(f"%{name}%"))

    if profession:
        query = query.filter(models.Person.primary_profession.ilike(f"%{profession}%"))

    if movie:
        query = query.join(models.Person.titles).filter(
            models.Title.primary_title.ilike(f"%{movie}%")
        )

    results = query.all()

    return [
        {
            "Primary Name": person.primary_name,
            "Birth Year": person.birth_year,
            "Death Year": person.death_year,
            "Profession": person.primary_profession,
            "Titles": [
                title.primary_title for title in person.titles
            ],
        }
        for person in results
    ]
