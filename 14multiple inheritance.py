class A:
    def class_a_method(self):
        return "I'm just a class A method"
class B:
    def class_b_method(self):
        return "I'm just a class B method"

class C(A,B):#multiple inheritance
    pass

obj=C()
print(obj.class_a_method())
print(obj.class_b_method())