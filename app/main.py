from fastapi import FastAPI
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routers import products

app = FastAPI(title="Ecommerce API")

app.include_router(products.router, prefix="/products", tags=["Products"])

@app.get("/")
def root():
    return {"message": "FastAPI on Lambda!"}
