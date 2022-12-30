# can we derive more than one class from base class---> yes
# multilevel inheritance

# method resolution order (MRO)
# how python use to check and find out the answers\



# method overriding
# isinstance(), it will take two argument to verify that instance is  part of that class or not
#issubclass()----


# here's the example of multilevel inheritance
class Grand:
    def __init__(self,name,cast,age):
        self.name=name
        self.cast=cast
        self.age=age

    def fullname(self):
        return f"{self.name} {self.cast}"
    
class Father(Grand):
    def __init__(self,name,cast,age,son):
        super().__init__(name,cast,age)
        self.son=son
    def fullname(self):
        return f"{self.name} {self.cast} {self.age} {self.son}"
    
class Son(Father):
    def __init__(self,name,cast,age,son,hobby):
        super().__init__(name,cast,age,son)
        self.hobby=hobby

son1=Grand("Jay","Pandey",14)
print(son1.fullname())# Jay Pandey

# print(help(Son))# here's to check method resolution order ... it will tell you how python will navigate through different classed and bring out the final result


obj=Son("Harsh","Mishra",19,"Ansh","Cricket")
print(obj.fullname())#Harsh Mishra 19 Ansh

print(isinstance(obj,Son))#True
print(isinstance(obj,Grand))#True because we had inherited Grand therefore it will be also object of Grand
print(isinstance(son1,Son))#False because it's object of Grand 

print(issubclass(Son,Father))#True
print(issubclass(Father,Grand))#True
print(issubclass(Grand,Father))#False
print(issubclass(Father,Son))#False
