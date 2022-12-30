# we use class keyword to define a class and according to convention always write the first letter of the name of your class in capital letter
# init method or constructor
class Person:
    def __init__(self,first_name,last_name,age):#attributes of the object and here self represent obect
        #instance variable
        self.frst_name=first_name
        self.lst_name=last_name
        self.age=age
#creating object
p1=Person("Mohit","Dwivedi",20)
p2=Person("Harshit","Dwivedi",20)
# print(p1.first_name) it will show error because we haven't define first_name attribute we had define frst_name attribute
print(p2.frst_name)
print(p1.lst_name)
# and init method or constructor will be called whenever you make an object 
# and at the place of self you can write whatever you want but according to convention self should be used