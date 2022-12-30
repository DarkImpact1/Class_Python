class Circle:
    inst=0
    pi=3.14# declaring class varible/class attribute
    def __init__(self, radius):
        Circle.inst+=1
        self.radius=radius

    def Area(self):
        return Circle.pi*self.radius*self.radius
    
    def Circumference(self):
        return format(2*Circle.pi*self.radius,".3f")
    
    @classmethod
    def func1(cls):
        return f"here I'm returning total number of instance created..{cls.inst} of {cls.__name__} class"
    
    

    
a=Circle(5)
b=Circle(6)
print(Circle.func1())


