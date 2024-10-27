from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Pydantic model for request body validation
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

app = FastAPI()

# Keep the root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Implement the PUT endpoint
@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    q: Optional[str] = None
):
    # Create response dictionary with item_id and all fields from the request body
    response = {
        "item_id": item_id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "tax": item.tax
    }
    
    # Add query parameter to response if it exists
    if q:
        response["q"] = q 
    return response
