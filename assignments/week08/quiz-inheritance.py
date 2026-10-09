""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:

    def __init__(self ,brand,model,year):
        self.brand = brand
        self.model = model
        self.year  = year

    def get_info():
        return ("This is vehile info{self.brand} model is {self.model} yesr is {self.year}")
class car(Vehicle):
    def __init__(self,brand,model,year,Number_of_door):
        super().__init__(brand,model,year)
        self.Number_of_door = Number_of_door

    def car_info():
        return ("This is vehile info{self.brand} model is {self.model} yesr is {self.year}")
    

vehicle = Vehicle("Honda","civic","1001")
print(Vehicle.get_info)