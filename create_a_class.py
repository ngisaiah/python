class Car:
    def __init__(self, name, make, year, num_of_doors):
        self.name = name
        self.make = make
        self.year = year
        self.num_of_doors = num_of_doors

    def vroom(self):
        print(f'A {self.name} flies by!')

m4 = Car('M4', 'BMW M4', 2025, 2)

print(m4.vroom())