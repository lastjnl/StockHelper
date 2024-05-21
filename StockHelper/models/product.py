class Product:

    def __init__(self, name, quantity=0):
        self.name = name
        if quantity == 0:
            self.quantity = 0
        else:
            self.quantity = quantity
                
    def to_dict(self):
        return {"name": self.name, "quantity": self.quantity}
    
    def add_quantity(self, quantity):
        self.quantity += quantity
        
    def remove_quantity(self, quantity):
        self.quantity -= quantity
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["quantity"])
                

        
