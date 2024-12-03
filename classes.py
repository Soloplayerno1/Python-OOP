# Class
class Vehicle:
    # Properties
    def __init__(self, make, model):
        self.make = make
        self.model = model
    # Method
    def moves(self):
        print("Move along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

# Object
my_car = Vehicle('Tesla', 'model 3')
my_car.get_make_model()
my_car.moves()

# Inheritance
class Airplane(Vehicle):
    # Overwrite the duplicated method, properties
    def __init__(self, make, model, id):
            # Inheriting properties that duplicated with the parent class
            super().__init__(make, model)
            self.id = id  

    def moves(self):
        print("Flies along...")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")