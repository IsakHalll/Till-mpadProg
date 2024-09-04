import os

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def view_car(self):
        return f"{self.make} - {self.model} - ({self.color})"
    

os.system("cls")

cars = []

while True:
    car_make = input("Make: ")
    car_model = input("Model: ")
    car_color = input("Color: ")
    
    cars.append(Car(car_make, car_model, car_color))
    for car in cars:
        print(car.view_car())
    