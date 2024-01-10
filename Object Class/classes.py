class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('moves along.....')

    def get_make_model(self):
        print(f"I m a {self.make} and  {self.model}.")


my_car = Vehicle("tesla", "2302")
# print(my_car.make)
# print(my_car.model)

my_car.get_make_model()

my_car.moves()
