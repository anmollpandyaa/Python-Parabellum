class Expense:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def __repr__(self):
        return f"Product: {self.name}, Price: ₹{self.price}, Category: {self.category}"