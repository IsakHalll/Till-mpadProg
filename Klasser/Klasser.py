# class Car:
#     def __init__(self, name):
#         self.name = name



# car = Car("Toyota")

# print(car.name)

class Car:
    def __init__(self):
        self.car_details = {}

    def add_car(self, make, model):
        if make in self.car_details:
            self.car_details[make].append(model)
        else:
            self.car_details[make] = [model]


    def list_cars(self):
        order = 1
        for make,model in self.car_details.items():
            print(f"{order}){make} - {model}")
            order += 1
    

car = Car()
car.add_car("Toyota", "AE86")
car.add_car("Mazda", "FC3S")
car.add_car("Subaru", "Impreza wrx")
car.add_car("Toyota", "MR2")
car.list_cars()