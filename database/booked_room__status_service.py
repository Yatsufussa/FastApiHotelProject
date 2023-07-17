from database.models import BookingForm
from database import get_db
from datetime import datetime


def add_booked_room_db(hotel_id: int,
                       check_in: datetime,
                       check_out: datetime,
                       status: bool,
                       user_phone_number: int,
                       user_name: str,
                       user_reg_date: datetime,
                       hotel_name: str,
                       hotel_location: str,
                       hotel_state: str,
                       hotel_city: str,
                       hotel_country: str,
                       hotel_contact: str,
                       hotel_star: int,
                       hotels_card_number: int,
                       card_number: int,
                       card_name: str,
                       card_holder: str,
                       transaction_id: int):
    db = next(get_db())

    book_room = BookingForm(hotel_id=hotel_id,
                            check_in=check_in,
                            check_out=check_out,
                            status=status,
                            user_phone_number=user_phone_number,
                            user_name=user_name,
                            user_reg_date=user_reg_date,
                            hotel_name=hotel_name,
                            hotel_location=hotel_location,
                            hotel_state=hotel_state,
                            hotel_city=hotel_city,
                            hotel_country=hotel_country,
                            hotel_contact=hotel_contact,
                            hotel_star=hotel_star,
                            hotels_card_number=hotels_card_number,
                            card_number=card_number,
                            card_name=card_name,
                            card_holder=card_holder,
                            transaction_id=transaction_id)
    db.add(book_room)
    db.commit()
    return True


def delete_booked_room_db(status: bool):
    db = next(get_db())
    room = db.query(BookingForm).filter_by(staus=status).first()
    if room:
        db.delete(room)
        db.commit()
        return False
    else:
        return True