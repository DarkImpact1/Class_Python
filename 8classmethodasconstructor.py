class Person:

    def __init__(self, fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        
    def fullname(self):
        return f"full name is {self.fname} {self.lname}"
    @classmethod
    def from_string(cls,string):
        fname,lname,age=string.split(",")
        return cls(fname,lname,age)# created an object using class method as constructor
    
p1=Person("Mohit","Dwivedi",20)#creating first object using __init__ constructor

p2=Person.from_string("Harshit,dwivedi,20")#creating object using class method as constructor..
print(p1.fullname())
print(p2.fullname())