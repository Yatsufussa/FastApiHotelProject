from main import app
from database import add_apartment_db, add_hotel_db

@app.post('/add_hotel')
async def add_hotel_api(hotel_name: str,
                        hotel_location: str,
                        hotel_state: str,
                        hotel_city: str,
                        hotel_country: str,
                        hotel_contact: str,
                        hotel_star: int,
                        hotels_card_number: int):
    result = add_hotel_db(hotel_name=hotel_name,
                          hotel_location=hotel_location,
                          hotel_state=hotel_state,
                          hotel_city=hotel_city,
                          hotel_country=hotel_country,
                          hotel_contact=hotel_contact,
                          hotel_star=hotel_star,
                          hotels_card_number=hotels_card_number)

    return {"status": 1, "message": result}


@app.post('/add_apartment')
async def add_apartment_api(hotel_id: str,
                            apartments_number: int,
                            room_numbers: int,
                            room_amenity: str,
                            apartment_price: float,
                            status: bool):
    result = add_apartment_db(hotel_id=hotel_id,
                              apartments_number=apartments_number,
                              room_numbers=room_numbers,
                              room_amenity=room_amenity,
                              apartment_price=apartment_price,
                              status=status)
    return {"status": 1, "message": result}

