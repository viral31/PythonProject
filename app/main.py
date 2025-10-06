from fastapi import FastAPI
from app.routers import products

app = FastAPI(title="Ecommerce API")

app.include_router(products.router, prefix="/products", tags=["Products"])
