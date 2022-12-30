class Person:
    def __init__(self,fname,lname,age="not provided"):
        self.first_name=fname
        self.last_name=lname
        self.age=age

    def full_name(self):# here we defined a method named full name and we can use it with any object
        return f"{self.first_name} {self.last_name}"
    
p1=Person("mohit","dwivedi",20)
p2=Person("harshit","dwivedi")

print(p1.full_name())#here we are using full name method which we had defined in our class
print(Person.full_name(p2))

print(p2.age)
