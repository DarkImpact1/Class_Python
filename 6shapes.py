class Shapes:
    pi=3.14
    def __init__(self,side=None,side2=None):
        self.radius=side
        self.length=side
        self.breadth=side2
        self.side=side
        self.base=side
        self.height=side2
    
    def Areacircle(self):
        return f"{Shapes.pi*self.radius*self.radius} squnit"
    
    def Perimetercircle(self):
        return f"{2*Shapes.pi*self.radius} unit"
    
    def Arearectangle(self):
        return f"{self.length*self.breadth} squnit"
    
    def Perimeterrectangle(self):
        return f"{2*(self.length+self.breadth)} unit"
    
    def Areasquare(self):
        return f"{self.side**2} squnit"
    
    def Perimetersquare(self):
        return f"{4*self.side} unit"
    
    def Areatriangle(self):
        return f"{0.5*self.base*self.height} squnit"

# print("currently you have to options circle,rectangle and square")    
# shape=input("Enter the shape of which you want to calculater area or perimeter:\t").lower().strip()
# choice=input("what do want to calculate Area or Circumference/perimeter:\t").lower().strip()
# if shape=="circle":
#     radius=int(input("Enter the radius of circle:\t "))
#     c1=Shapes(radius)
#     if choice=="area":
#         print(c1.Areacircle())
#     elif choice=="circumference" or choice=="perimeter":
#         print(c1.Perimetercircle())
# elif shape=="rectangle":
#     l=int(input("Enter length :\t"))
#     b=int(input("Enter breadth :\t"))
#     R=Shapes(l,b)
#     if choice=="area":
#         print(R.Arearectangle())
#     elif choice=="perimeter" or choice=="circumference":
#         print(R.Perimeterrectangle())

# elif shape=="square":
#     side=int(input("Enter side of square:\t"))
#     S=Shapes(side)
#     if choice=="area":
#         print(S.Areasquare())
#     elif choice=="perimeter":
#         print(S.Perimetersquare())

square1=Shapes(30)
print(square1.Areasquare())
triangle=Shapes(10,10)
print(triangle.Areatriangle())
t=Shapes()
print(t.Areatriangle)