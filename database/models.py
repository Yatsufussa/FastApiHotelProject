from database import Base
from sqlalchemy import Column, String, Integer, Float, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    user_phone_number = Column(Integer, nullable=False)
    user_email = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    user_reg_date = Column(DateTime, default=datetime.now())

class Password(Base):
    __tablename__ = 'passwords'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    password = Column(String, nullable=False)

    user_fk = relationship(User)

class Card(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    card_number = Column(Integer, nullable=False)
    card_name = Column(String)
    card_holder = Column(String)
    card_exp_date = Column(Integer, nullable=False)
    card_balance = Column(Float)
    card_added_date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User)

class Hotel(Base):
    __tablename__ = 'hotels'
    hotel_id = Column(Integer, autoincrement=True, primary_key=True)
    hotel_name = Column(String, nullable=False)
    hotel_location = Column(String, nullable=False)
    hotel_state = Column(String, nullable=False)
    hotel_city = Column(String, nullable=False)
    hotel_country = Column(String, nullable=False)
    hotel_contact = Column(String)
    hotel_star = Column(Integer)
    hotels_card_number = Column(Integer, nullable=False)


class Apartments(Base):
    __tablename__ = 'apartments'
    hotel_id = Column(Integer, ForeignKey('hotels.hotel_id'), nullable=False)
    apartments_number = Column(Integer, autoincrement=True, primary_key=True)
    room_numbers = Column(Integer, nullable=False)
    room_amenity = Column(String, nullable=False)
    apartment_price = Column(Float, nullable=False)
    status = Column(Boolean, nullable=False)

    hotel_fk = relationship(Hotel)


class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, autoincrement=True, primary_key=True)
    card_from = Column(Integer, ForeignKey('cards.card_id'), nullable=False)
    amount = Column(Float, nullable=False)
    card_to = Column(Integer, ForeignKey('hotels.hotel_id'), nullable=False)
    tansaction_date = Column(DateTime, default=datetime.now())

    card_fk = relationship(Card)
    hotel_fk = relationship(Hotel)


class BookingForm(Base):
    __tablename__ = 'booking'
    hotel_id = Column(Integer,autoincrement=True,primary_key=True)
    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    status = Column(Boolean, ForeignKey('apartments.status'), nullable=False)
    user_phone_number = Column(Integer, ForeignKey('users.user_phone_number'), nullable=False)
    user_email = Column(String, ForeignKey('users.user_email'),  nullable=False)
    user_name = Column(String, ForeignKey('users.user_name'), nullable=False)
    user_reg_date = Column(DateTime, ForeignKey('users.user_reg_date'), default=datetime.now())
    hotel_name = Column(String, ForeignKey('hotels.hotel_name'), nullable=False)
    hotel_location = Column(String, ForeignKey('hotels.hotel_location'), nullable=False)
    hotel_state = Column(String, ForeignKey('hotels.hotel_state'), nullable=False)
    hotel_city = Column(String, ForeignKey('hotels.hotel_city'), nullable=False)
    hotel_country = Column(String, ForeignKey('hotels.hotel_country'), nullable=False)
    hotel_contact = Column(String, ForeignKey('hotels.hotel_contact'))
    hotel_star = Column(Integer, ForeignKey('hotels.hotel_star'),)
    hotels_card_number = Column(Integer, ForeignKey('hotels.hotels_card_number'), nullable=False)
    card_number = Column(Integer, ForeignKey('cards.card_number'), nullable=False)
    card_name = Column(String, ForeignKey('cards.card_name'))
    card_holder = Column(String,  ForeignKey('cards.card_holder'))
    transaction_id = Column(Integer, ForeignKey('transactions.transaction_id'))

    hotel_fk = relationship(Hotel)
    user_fk = relationship(User)
    apartments_fk = relationship(Apartments)
    transaction_fk = relationship(Transaction)
    card_fk = relationship(Card)

