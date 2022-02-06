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
    result = collection.find_one({"name":name}, {"_id":0})
    if result != None:
        return {
            "status": "found",
            "result": result
        }
    else:
        raise HTTPException(404, f"Couldn't find reservation with name: {name}'")

@app.get("/reservation/by-table/{table}")
def get_reservation_by_table(table: int):
    result = collection.find({"table_number":int(table)}, {"_id":0})
    lst_result = list(result)
    if len(lst_result) != 0:
        final = json.loads(json_util.dumps(lst_result))
        return {
            "status": "found",
            "result": final
        }
    else:
        raise HTTPException(404, f"Couldn't find reservation with name: {table}'")

@app.post("/reservation")
def reserve(reservation : Reservation):
    result = collection.find({"time":reservation.time, "table_number": reservation.table_number})
    size = len(list(result))
    if size == 0:
        reserve = jsonable_encoder(reservation)
        collection.insert_one(reserve)
    else:
        raise HTTPException(404, f"{reservation.time} is already reserved")

@app.put("/reservation/update/{new_time}")
def update_reservation(reservation: Reservation, new_time: int):
    result = collection.find({"time":int(new_time), "table_number": reservation.table_number})
    lst_result = list(result)
    if len(lst_result) == 0:
        my_query = {"time":reservation.time, "table_number": reservation.table_number}
        new_query = {"$set":{"time":new_time}}
        collection.update_one(my_query, new_query)
    else:
        return HTTPException(404, f"Reservation time is already reserved at: {reservation.time}'")
    

@app.delete("/reservation/delete/{name}/{table_number}")
def cancel_reservation(name: str, table_number : int):
    collection.delete_one({"name":name, "table_number":table_number})

