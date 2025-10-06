from fastapi import APIRouter, HTTPException
from app.schemas.product import Product
from typing import List

router = APIRouter()

# Hardcoded product data
products = [
    Product(id=1, name="Laptop", description="A powerful laptop", price=1200.0, in_stock=True),
    Product(id=2, name="Phone", description="A smart phone", price=800.0, in_stock=True),
    Product(id=3, name="Headphones", description="Noise cancelling", price=150.0, in_stock=False),
]

@router.get("/", response_model=List[Product])
def get_products():
    return products

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    for idx, product in enumerate(products):
        if product.id == product_id:
            products[idx] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/{product_id}")
def delete_product(product_id: int):
    for idx, product in enumerate(products):
        if product.id == product_id:
            del products[idx]
            return {"detail": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")
