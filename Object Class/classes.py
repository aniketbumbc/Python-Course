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


### Inheritance ####


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies Along.....')


class Truk (Vehicle):
    def moves(self):
        print('slow speed Along.....')


class Car (Vehicle):
    pass


vistara = Airplane('india Vistara', 'A623', 'FAA929')
mack = Truk('india mack', 'B623')
small_car = Car('Tata', 'Nano')


vistara.moves()
vistara.get_make_model()


mack.moves()
mack.get_make_model()

small_car.moves()
small_car.get_make_model()


# Plolymorphrism
