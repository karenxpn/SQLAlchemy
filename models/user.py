from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship

from models.base import TimeStampedModel


class User(TimeStampedModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False, unique=True)

    preference = Relationship('Preference', back_populates='user', uselist=False, passive_deletes=True)
    addresses = Relationship('Address', back_populates='user', passive_deletes=True)

    def __repr__(self):
        return f'<User(id={self.id}, first_name={self.first_name}, last_name={self.last_name})>'


class Preference(TimeStampedModel):
    __tablename__ = 'preferences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    language = Column(String(80), nullable=False)
    currency = Column(String(3), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True, unique=True)

    user = Relationship('User', back_populates='preference')


class Address(TimeStampedModel):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    road_name = Column(String(80), nullable=False)
    postcode = Column(String(80), nullable=False)
    city = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)

    user = Relationship('User', back_populates='addresses')

