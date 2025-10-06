import json
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="Ecommerce API")

@app.get("/")
def root():
    return {"message": "FastAPI on Lambda!"}

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop", "price": 1200.0},
        {"id": 2, "name": "Phone", "price": 800.0}
    ]

# Lambda handler
handler = Mangum(app)