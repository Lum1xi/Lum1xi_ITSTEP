class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}), {self.mileage} км"

class Owner:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        print(f"Автомобілі {self.name}:")

        for car in self.cars:
            print(f"- {car}")

owner = Owner("Олександр")
car1 = Car("Lol", "Kek", 2035, 3000000)
car2 = Car("kek", "Lol", 2018, 5190000)

owner.add_car(car1)
owner.add_car(car2)
owner.show_cars()
