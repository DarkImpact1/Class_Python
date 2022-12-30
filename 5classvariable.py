class Circle:
    pi=3.14# declaring class varible
    def __init__(self, radius) -> None:
        self.radius=radius

    def Area(self):
        return Circle.pi*self.radius*self.radius
    
    def Circumference(self):
        return format(2*Circle.pi*self.radius,".3f")
    
c1=Circle(10)#passing 10 as a radius
c2=Circle(20)#passing 20 as a radius
print(c1.Area())
print(c2.Area())
print(c1.Circumference())
print(c2.Circumference())