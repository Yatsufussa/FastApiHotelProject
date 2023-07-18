from fastapi import FastAPI
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

from hotel import hotel_api
from guest import guest_api
from card import card_api
from booked_rooms import booked_rooms_api

# Start Fast Api
# uvicorn main:app --reload
# if __name__ == '__main__':
#     app.run(debug=True)