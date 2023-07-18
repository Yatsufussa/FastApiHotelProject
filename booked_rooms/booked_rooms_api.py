from main import app
from database.booked_room__status_service import add_booked_room_db, delete_booked_room_db
from datetime import datetime


@app.post('/add_booked_room')
async def add_booked_room_api(booking_id: int,
                              check_in: datetime,
                              check_out: datetime,
                              user_id: int):
    result = add_booked_room_db(booking_id=booking_id,
                                check_in=check_in,
                                check_out=check_out,
                                user_id= user_id)
    return {"status": 1, "message": result}


@app.delete('/delete_booked_room')
async def delete_booked_room_api(booking_id:  int):
    result = delete_booked_room_db(booking_id=booking_id)
    return {"status": 1, "message": result}
