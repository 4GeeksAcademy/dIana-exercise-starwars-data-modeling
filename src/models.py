import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Planets(Base):
    __tablename__ = 'planets'
    ID = Column(Integer, primary_key=True)
    planet_name = Column(String(20))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    gravity = Column(Integer)
    terrain = Column(String(20))

class Starships(Base):
    __tablename__ = 'starships'
    ID = Column(Integer, primary_key=True)
    starship_name = Column(String(20)) 
    model = Column(String(20))
    starship_class = Column(String(20))
    length = Column(Integer)
    crew = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    ID = Column(Integer, primary_key=True)
    character_name = Column(String(20), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    planet = Column(String(20), ForeignKey('planets.ID'), unique=True)
    planets = relationship(Planets)
    starship = Column(String(20), ForeignKey('starships.ID'), unique=True)
    starships = relationship(Starships)


class Favorite_Character(Base):
    __tablename__ = 'favorite_character'
    ID = Column(Integer, primary_key=True)
    character_ID = Column(Integer, ForeignKey('characters.ID'))
    characters = relationship(Characters)

class Favorite_Planet(Base):
    __tablename__ = 'favorite_planet'
    ID = Column(Integer, primary_key=True)
    planet_ID = Column(Integer, ForeignKey('planets.ID'))
    planets = relationship(Planets)

class Favorite_Starship(Base):
    __tablename__ = 'favorite_starship'
    ID = Column(Integer, primary_key=True)
    starship_ID = Column(Integer, ForeignKey('starships.ID'))
    starships = relationship(Starships)

class Favorites(Base):
    __tablename__ = "favorites"
    ID = Column(Integer, primary_key=True)
    favorite_character_ID = Column(Integer, ForeignKey("favorite_character.ID"), unique=True)
    favorite_character = relationship(Favorite_Character)
    favorite_planet_ID = Column(Integer, ForeignKey("favorite_planet.ID"), unique=True)
    favorite_planets = relationship(Favorite_Planet)
    favorite_starship_ID = Column(Integer, ForeignKey("favorite_starship.ID"), unique=True)
    favorite_starship = relationship(Favorite_Starship)


class User(Base):
    __tablename__ = "user"
    ID = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = Column(String(20))
    email = Column(String(30), unique=True)
    favorites_ID = Column(Integer, ForeignKey("favorites.ID"), unique=True)
    favorites = relationship(Favorites)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
