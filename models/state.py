#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state", cascade="all,delete")

    @property
    def cities(self):
        """Method to get all the cities"""
        cities = models.storage.all(City)
        all_cities = []
        for value in cities.values():
            if self.id == value.state_id:
                all_cities.append(value)
        return all_cities
