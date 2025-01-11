class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return {'make' : self.make, 'model' : self.model}

class Car(Vehicle):
    def __init__(self,make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return {**super().get_info(), **{"fuel type" : self.fuel_type}}

v = Vehicle("Ural", "bike")
c = Car("Ford", "F150", "diesel")

print(v.get_info(),c.get_info(),sep='\n')
