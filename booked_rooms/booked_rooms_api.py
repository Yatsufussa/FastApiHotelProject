from main import app
from database.booked_room__status_service import add_booked_room_db, delete_booked_room_db
from datetime import datetime


@app.post('/add_booked_room')
async def add_booked_room_api(hotel_id: int,
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
    result = add_booked_room_db(hotel_id=hotel_id,
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

    return {"status": 1, "message": result}


@app.delete('/delete_booked_room')
async def delete_booked_room_api(status: bool):
    result = delete_booked_room_db(status=status)
    return {"status": 1, "message": result}
