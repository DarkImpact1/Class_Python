class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)# now if user give -ve price of any phone it will be 0
        # if price>0:
        #     self._price=price
        # else:
        #     self.price=0
    @property   
    def complete(self):
        return f"{self.brand} {self.model} and {self.price}"
    
    @property
    def priceupdate(self):
        return self._price
    
    @priceupdate.setter
    def newprice(self,nprice):
        self._price=max(nprice,0)

    def make_a_call(self,phone_number):
        return f"calling...... {phone_number}"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
phone=Phone("redmi","pro",1000)

print(phone.complete)# we don't have to use complete() because we had used @property decorator.....

# to update some value we use getter() and setter() in another language... and in python we use property decorator and setter()

phone._price=-500
print(phone.complete)