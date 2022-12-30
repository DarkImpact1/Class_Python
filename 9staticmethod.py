class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def nameage(self):
        return f"{self.name}'s age is {self.age}"
    
    # while defining any function we have to pass atleast one argument like self or cls so to define a function which wouldn't take any argument we have staticmethod decorator

    @staticmethod
    # it don't have any realtion with our class or instance but have some logical connection to class
    def func():
        return f"static method called"
    
p1=Person("mohit",14)
print(p1.func())