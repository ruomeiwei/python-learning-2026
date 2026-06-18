class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def describe(self):

        return f'This is a car. Make: {self.make}; Model: {self.model}'


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year 
    
    def describe(self):
        return f'This is a car. Make: {self.make}; Model: {self.model}; Year: {self.year}'

car = Car('Y', 'Z', 2020)

print(car.describe())