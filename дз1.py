class Car:
    def __init__(self, brand, model, year, color ):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    def display_info(self):
        print(self.brand, self.model, self.year, self.color)

car1 = Car("Toyota", "Camry", 2020, "Gray")
car2 = Car("BMW", "X5", 2022, "Black")
car3 = Car("Tesla", "Model 3", 2021, "White")

car1.display_info()
car2.display_info()
car3.display_info()