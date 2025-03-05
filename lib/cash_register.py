class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0  

    def add_item(self, title, price, quantity=1):
        """Adds an item to the register, updating the total and items list."""
        self.last_transaction_amount = price * quantity  
        self.total += self.last_transaction_amount
        self.items.extend([title] * quantity)  

    def apply_discount(self):
        """Applies the discount to the total price."""
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Subtracts the last item from the total."""
        self.total -= self.last_transaction_amount
     
        if self.last_transaction_amount > 0:
    
            for item in reversed(self.items):
                if self.last_transaction_amount == self.last_transaction_amount / len(self.items):
                    self.items.remove(item)
                    break
            self.last_transaction_amount = 0  
