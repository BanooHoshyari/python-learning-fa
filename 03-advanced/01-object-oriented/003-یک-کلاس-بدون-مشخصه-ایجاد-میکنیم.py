# یک کلاس بدون مشخصه ایجاد میکنیم
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car = Vehicle(220, 15000)
print("Max speed:", car.max_speed)
print("Mileage:", car.mileage)