import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    Id = Column(Integer, primary_key = True)
    Username = Column(String(20), nullable = False, unique = True)
    Email = Column(String(20), nullable = False, unique = True)

    def serialize (self):
        return {
            "Id": self.Id,
            "Username": self.Username,
            "Email": self.Email
        }

class People(Base):
    __tablename__ = 'People'

    Id = Column(Integer, primary_key = True)
    Name = Column(String(20), nullable = False, unique= True)
    Planet = Column(String(20), ForeignKey("Planets.Name"))
    People = Column(String(20), ForeignKey("User.People"))

    def serialize (self):
        return {
            "Id": self.Id,
            "Name": self.Name,
            "Planet": self.Planet,
            "People": self.People
        }

class Planet(Base):
    __tablename__ = 'Planets'
    
    Id = Column(Integer, primary_key = True)
    Name = Column(String(20), nullable = False, unique = True)

    def serialize (self):
        return {
            "Id": self.Id,
            "Name": self.Name
        }
        
class Favorites(Base):
    __tablename__ = 'Favorites'

    Id = Column(Integer, primary_key=True)
    PeopleId = Column(Integer, ForeignKey("People.Id"))
    PlanetId = Column(Integer, ForeignKey("Planets.Id"))
    UserId = Column(Integer, ForeignKey("User.Id"))

    def serialize (self):
        
        return {
            "Id": self.Id,
            "PeopleId": self.PeopleId,
            "PlanetId": self.PlanetId,
            "UserId": self.UserId
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
