class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def get_info(self):
        return self.make, self.model

print(Vehicle('chetirka','vaz-2114').get_info())

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return super().get_info(), self.fuel_type
    
print(Car('chetirka','vaz-2114','a92').get_info())