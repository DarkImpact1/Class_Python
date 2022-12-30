class Bike:
    def __init__(self, name,price,average ) -> None:
        self.name=name
        self.price=price
        self.average=average

bike1=Bike("Pulsar",85000, "40kmpl")
bike2=Bike("Apache",105000, "35kmpl")
bike3=Bike("Bullet",155000, "30kmpl")

print(bike1.name)
print(bike1.price)
print(bike1.average)
print(bike2.name)
print(bike2.price)
print(bike2.average)
print(bike3.name)
print(bike3.price)
print(bike3.average)