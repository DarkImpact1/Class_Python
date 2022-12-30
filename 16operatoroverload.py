class A:
    def __init__(self,n):
        self.a=n
    

    def __add__(self,other):
        return self.a + other.a
    
a=A(5)
b=A(6)
print(a+b)# it will print the sum of 