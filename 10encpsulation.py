# Encapsulation
# creating class and its method at a place and bind it together at a same place is simply called as encapsulation

# Abstraction
# hiding complexity from user and performing all the actions like .... we use sort method from list so list use different alogorithm and finally give output

# some special naming convention
# _name  ----> putting underscore just before any name means that it's private don't do anything from this variable.. it's kind of private name ... It's just a convention..

# like .... __name__ or _name_ these type of name is called dunder/magic methods

# Name Mangling


class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.__price=price

    def make_a_call(self,phone_number):
        return f"calling...... {phone_number}"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
phone1=Phone("Realme","Narzo20a",1000)
# print(phone1.__price) --> it will show error because python has changed __price to _Phone__price
print(phone1.__dict__)
# {'brand': 'Realme', 'model': 'Narzo20a', '_Phone__price': 1000}
print(phone1._Phone__price)