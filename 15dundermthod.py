# special magic method or dunder methods are those methods which are preceded and followed by __
# like ... __init__ __dict__ etc

l=[1,2,3,4,5]
print(l)#--> [1, 2, 3, 4, 5]

class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def __str__(self):
        return f"{self.brand} {self.model} {self.price}"
    
obj=Phone("Realme","Narzo10",15000)
# print(obj)#<__main__.Phone object at 0x0000019756FC7880> before dunder __str__ defined
print(obj) #---> Realme Narzo10 15000 after dunder is defined..
# Basically there are two methods to print your created object..... first is __str__ another is __repr__ (representation)

class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    # repr is used basically used by developers by which if anyone copies this object then as a result it will again create an object
    def __repr__(self):
        return f"Phone('{self.brand}','{self.model}',{self.price})"
    
    def phonename(self):
        return f"{self.brand} {self.model}"
    #creating len method
    def __len__(self):
        return len(self.phonename())
    
obj2=Phone("Realme","GTneo3T",33000)
print(obj2)
# print(obj2.__leng__())
print(len(obj2))
#-----------------------------------------------------------------------------------------------------
