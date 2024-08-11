from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Association tables
title_person_association = Table(
    "title_person",
    Base.metadata,
    Column("title_id", Integer, ForeignKey("titles.id")),
    Column("person_id", Integer, ForeignKey("people.id")),
)

title_genre_association = Table(
    "title_genre",
    Base.metadata,
    Column("title_id", Integer, ForeignKey("titles.id")),
    Column("genre_id", Integer, ForeignKey("genres.id")),
)


class Title(Base):
    __tablename__ = "titles"

    id = Column(Integer, autoincrement=True, primary_key=True)
    title_id = Column(String, unique=True, index=True)
    title_type = Column(String)
    primary_title = Column(String, index=True)
    original_title = Column(String)
    is_adult = Column(Boolean, default=False)
    start_year = Column(Integer, index=True)
    end_year = Column(Integer, nullable=True)
    runtime_minutes = Column(Integer)
    genres = relationship(
        "Genre", secondary=title_genre_association, back_populates="titles"
    )
    people = relationship(
        "Person", secondary=title_person_association, back_populates="titles"
    )


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, autoincrement=True)
    person_id = Column(String, unique=True, index=True)
    primary_name = Column(String, index=True)
    birth_year = Column(Integer)
    death_year = Column(Integer, nullable=True)
    primary_profession = Column(String)
    titles = relationship(
        "Title", secondary=title_person_association, back_populates="people"
    )


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    titles = relationship(
        "Title", secondary=title_genre_association, back_populates="genres"
    )
