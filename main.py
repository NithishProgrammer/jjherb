import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Define your data structure
class Item(BaseModel):
    Order_ID: str
    Customer: str
    Items: str
    WPhone: str
    Address: str
    Total: str
    Date: str

# Your SheetDB API URL
SHEETDB_URL = "https://sheetdb.io/api/v1/qnbb7uvfnbn2v"

@app.post("/post")
def post_data(entry: Item):
    # This wraps the incoming JSON into the "data" list SheetDB needs
    p_load = {"data": [entry.model_dump()]}
    
    # Send the POST request
    response = requests.post(SHEETDB_URL, json=p_load)
    
    # Return the result from SheetDB to your browser/frontend
    return response.json()