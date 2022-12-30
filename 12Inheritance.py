class Parent:
    def __init__(self,name,color,nation):
        self.name=name
        self.color=color
        self.nation=nation

    def detail(self):
        return f"{self.name} if from {self.nation} and his color is {self.color}"
    
class Child(Parent):# write the name of class inside the name of that class in which you want to inherit the property
    def __init__(self,name,color,nation,state,district,village):
        # Parent.__init__(self,name,color,nation)# instead of declaring instance variable just assingn these task to parent class 
        # another way to assign the task
        super().__init__(name,color,nation)# don't need to write self while using this method
        self.state=state
        self.district=district
        self.village=village

obj1=Parent("sam","white","africa")
obj2=Child("Dwayne","black","Southafrica","state","district","village")
print(obj1.detail())
print(obj2.detail(),obj2.state,obj2.district,obj2.village)


# the above way is uncommon way to inherit the property of parent class 