import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key = True)
    username = Column(String(20), nullable = False, unique = True)
    email = Column(String(20), nullable = False, unique = True)
    password = Column(String(20), nullable=False)
    name = Column(String (20), nullable = False)
    last_name = Column(String (20), nullable = False)

    def serialize (self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            "favorites": self.favorites
        }

class People(Base):
    __tablename__ = 'People'

    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False, unique= True)
    gender = Column(String(10), nullable = False)
    planet_id = Column(String(20), ForeignKey("Planets.id"))

    def serialize (self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "planet": self.planet
        }

class Planet(Base):
    __tablename__ = 'Planets'
    
    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False, unique = True)
    climate = Column(String(10), nullable = False)
    population = Column(Integer, nullable = False)


    def serialize (self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population
        }
        
class Favorites(Base):
    __tablename__ = 'Favorites'

    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey("People.id"))
    planet_id = Column(Integer, ForeignKey("Planets.id"))
    user_id = Column(Integer, ForeignKey("User.id"))

    def serialize (self):
        
        return {
            "id": self.Id,
            "people_id": self.people_id,
            "planet_id": self.planet_id,
            "user_id": self.user_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
