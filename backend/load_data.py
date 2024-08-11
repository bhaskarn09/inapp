import pandas as pd
from sqlalchemy.orm import sessionmaker
from app.models import Base, Title, Person, Genre
from app.database import engine

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

title_df = pd.read_csv("../title.small.tsv", sep="\t")
name_df = pd.read_csv("../name.small.tsv", sep="\t")

for _, row in title_df.iterrows():
    genres = row["genres"].split(",") if pd.notna(row["genres"]) else []
    genre_objects = []

    for genre_name in genres:
        genre = session.query(Genre).filter_by(name=genre_name).first()
        if not genre:
            genre = Genre(name=genre_name)
            session.add(genre)
        genre_objects.append(genre)

    title = Title(
        title_id=row["tconst"],
        title_type=row["titleType"],
        primary_title=row["primaryTitle"],
        original_title=row["originalTitle"],
        is_adult=bool(row["isAdult"]),
        start_year=int(row["startYear"]) if row["startYear"] != "\\N" else None,
        end_year=int(row["endYear"]) if row["endYear"] != "\\N" else None,
        runtime_minutes=(
            int(row["runtimeMinutes"]) if row["runtimeMinutes"] != "\\N" else None
        ),
        genres=genre_objects,
    )
    session.add(title)


for _, row in name_df.iterrows():
    known_titles = (
        row["knownForTitles"].split(",") if pd.notna(row["knownForTitles"]) else []
    )
    title_objects = []

    for title_id in known_titles:
        title = session.query(Title).filter_by(id=title_id).first()
        if title:
            title_objects.append(title)

    person = Person(
        person_id=row["nconst"],
        primary_name=row["primaryName"],
        birth_year=int(row["birthYear"]) if row["birthYear"] != "\\N" else None,
        death_year=int(row["deathYear"]) if row["deathYear"] != "\\N" else None,
        primary_profession=row["primaryProfession"],
        titles=title_objects,
    )
    session.add(person)

session.commit()

session.close()

print("Data loading complete.")
