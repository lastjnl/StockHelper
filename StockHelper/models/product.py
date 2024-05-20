from inventory import load_stock

class Product

    def __init__(self, name, quantity=0):
        self.name = name
        if quantity == 0
            self.load_quantity()
        else 
            self.quantity = quantity

    def load_quantity(self):
        stock = load_stock("data/stock.json")
        self.quantity = 0
        for item, quantity in stock.items()
            if item == self.name
                self.quantity = quantity
                

        
