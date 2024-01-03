# init - constructor that sets up class variables

class qtyordering:
    def __init__(self,qty):
        self.qty = qty
        self.price = 0 #doesnt need to be declared but can declare it like, called a type hint: self.price:float=0
        self.amount = 0
    
    def calc(self):
        if 0 <= self.qty <= 99:
            self.price = 5.95

        elif 99 < self.qty <= 199:
            self.price = 5.75
        
        elif 199 < self.qty <= 299:
            self.price = 5.40
        
        elif 299 < self.qty:
            self.price = 5.15
    
        self.amount = self.price*self.qty
    
    def __str__(self): #string dunder method
        return f"Quanity={self.qty}\nPrice=${self.price:.2f}\nAmount=${self.amount:.2f}"
    
    # def __repr__(self): #representation dunder method
    #    return f"\nQuanity={self.qty}\nPrice=${self.price:.2f}\nAmount=${self.amount:.2f}\n"
    
#prog213b