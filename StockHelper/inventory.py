import json

def load_stock(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_stock(filepath, stock):
    with open(filepath, 'w') as file:
        json.dump(stock, file, indent=4)

def add_item(stock, item, quantity):
    stock[item] = stock.get(item, 0) + quantity
    return stock

def remove_item(stock, item, quantity):
    if item in stock:
        stock[item] = max(0, stock[item] - quantity)
    return stock
