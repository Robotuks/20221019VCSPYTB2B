# class definition
class Car:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

        self.engine_status = False
        self.oil_level = 0.0
        self.MAX_OIL_LEVEL = 3.2

    def __str__(self) -> str:
        return f'Brand: {self.brand}, year: {self.year}, color: {self.color}'

    def start_engine(self):
        if self.engine_status == False:
            self.engine_status = True

    def stop_engine(self):
        if self.engine_status == True:
            self.engine_status = False

    def add_oil(self, oil_amount):
        if self.oil_level + oil_amount > self.MAX_OIL_LEVEL:
            self.oil_level = self.MAX_OIL_LEVEL
        else:
            self.oil_level += oil_amount

# creation of class instances
car_1 = Car('BMW', 2006, 'black')
print('car_1')
print('engine status:', car_1.engine_status)
print (car_1)
car_1.start_engine()
print('engine status:', car_1.engine_status)
print('oil level:', car_1.oil_level)
car_1.add_oil(1.5)
print('oil level:', car_1.oil_level)
car_1.add_oil(3)
print('oil level:', car_1.oil_level)
# print (car_1.brand )
# print (car_1.year )
# print (car_1.color )

car_2 = Car('Tesla', 2015, 'Silver')
print('car_2')
print('oil level:', car_2.oil_level)
car_2.add_oil(2.3)
print('oil level:', car_2.oil_level)

print (car_2)
# print (car_2.brand )
# print (car_2.year )
# print (car_2.color )