my_list =  [1, 6, 8]
print(my_list)
my_list.append(67)
# print(my_list[2])
# for i in range(4):
#     print(my_list[i])

# def my_func(name, age):
#     print(f"{name} is {age} years old")
# my_func("John", 23)

# def my_func(name, age):
#     return (f"{name} is {age} years old")
# print(my_func("John", 23))

# def mmm(*args):
#     print(args)
# mmm(1,4,6,87,"ffff")






class Human:
    def __init__(self, name= "Human"):
        self.name = name

class auto:
    def __init__(self, brend):
        self.brend = brend
        self.passangers = []

    def add_passanger(self, human):
        self.passangers.append(human)

    def print_passanger(self):
        if self.passangers != []:
            print(f"В автомобілі {self.brend} зареєстровані такі пасажири:")
            for i in self.passangers:
                print(i.name)
        else:
            print("пасажирів нема(")

ann = Human ("Ann")
nick = Human ("Nick")

car = auto("tayota")

car.add_passanger(ann)
car.add_passanger(nick)

car.print_passanger()