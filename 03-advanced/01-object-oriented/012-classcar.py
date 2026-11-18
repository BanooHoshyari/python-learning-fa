from heater import Heater
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        self.heater = Heater()
    def stop_(self):
        print(f"the {self.name} car is stopped")
    def heater_on(self):
        self.heater.on_()
        self.heater.warmig_on(20)
car = Car("benz", model=2022, color="red")
car.heater_on()