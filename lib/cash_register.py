#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount  
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):  
        return self._discount
    
    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value  
        else:
            print("Not valid discount")  
            self._discount = 0

    def add_item(self, item, price, quantity):
        self.total += price * quantity
    
        
        
        self.items.append({
            "Item": item,
            "price": price,
            "quantity": quantity,
            "Total": self.total
        })
        
        
        transaction = {
            "Item": item,
            "price": price,
            "quantity": quantity
        }
       
    def apply_discount(self):
        
        if self.discount > 0:
            self.total = self.total * ((100 - self.discount) / 100)
            print(f"Applied {self.discount}% discount. Total: ${self.total:.2f}")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        
        if self.previous_transactions:
            removed = self.previous_transactions.pop()
            self.total -= removed["price"] * removed["quantity"]
            self.items.pop()
            print(f"Removed: {removed['quantity']}x {removed['Item']}")
        else:
            print("No transactions to void")

    