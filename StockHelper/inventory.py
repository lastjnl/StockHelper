import os
import sys
import json

from models.product import Product

def load_stock(filepath, search_string=""):
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return []
    
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            stock = []
            for item in data:
                if search_string:
                    if search_string == item["name"] or search_string in item["name"]:
                        stock.append(Product.from_dict(item))
                else:
                    stock.append(Product.from_dict(item))
                    
            return stock
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_stock(filepath, stock):
    with open(filepath, 'w') as file:
        json.dump([product.to_dict() for product in stock], file, indent=4)

def add_item(stock, product):
    existing_product = find_product(stock, product.name)
    if existing_product:
        existing_product.add_quantity(product.quantity)
    else:
        stock.append(product)
    return stock

def remove_item(stock, product):
    existing_product = find_product(stock, product.name)
    if existing_product:
        existing_product.remove_quantity(product.quantity)
    return stock

def find_product(stock, name):
    for product in stock:
        if product.name == name:
            return product
    return None
