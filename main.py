import json

from fastapi import FastAPI, HTTPException
from bson import json_util
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

class Reservation(BaseModel):
    name : str
    time: int
    table_number: int
    
client = MongoClient('mongodb://localhost', 27017)

# TODO fill in database name
db = client["test"]

# TODO fill in collection name
collection = db["test"]

app = FastAPI()


# TODO complete all endpoint.
@app.get("/reservation/by-name/{name}")
def get_reservation_by_name(name:str):
    pass

@app.get("reservation/by-table/{table}")
def get_reservation_by_table(table: int):
    pass

@app.post("/reservation")
def reserve(reservation : Reservation):
    result = collection.find({"time": {"$eq": reservation.time}, "table_number": reservation.table_number})
    size = len(list(result))
    if size == 0:
        reserve = jsonable_encoder(reservation)
        collection.insert_one(reserve)
    else:
        raise HTTPException(404, f"{reservation.time} is already reserved")

@app.put("/reservation/update/")
def update_reservation(reservation: Reservation):
    pass

@app.delete("/reservation/delete/{name}/{table_number}")
def cancel_reservation(name: str, table_number : int):
    pass

