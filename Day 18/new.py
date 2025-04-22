#inheritance -> 

#employee -> programmer employee
#id, task  -> id, task, programming

#father -> son
#height, face card -> height, face card, active in computer

class Employee:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def show(self):
        print(f'name is {self.name} and tasks as given : {self.task}')

class Programmer(Employee):
    def __init__(self, name, task, lang):
        super().__init__(name, task)
        # self.name = name
        # self.task = task
        self.lang = lang

    def show(self):
        print(f'lang is {self.lang}')

# a = Employee('Mohit', True)
# a.show()

# b = Programmer('Rajat', True, 'Java Script')
# b.show()


class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'the name is {self.name}')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def info(self):
        print(f'the name is {self.name} and the breed is {self.breed}')

# a = Animal('Bruno')
# a.show()

# b = Dog('Champak', 'German Shepherd')
# b.show()
# b.info()

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def info(self):
        print(f'this is a vehicle with {self.wheels} wheels')

class Bike(Vehicle):
    def __init__(self, wheels, speed):
        super().__init__(wheels)
        self.speed = speed

    def show(self):
        print(f'the speed is {self.speed}kmph')

a = Vehicle(4)
a.info()
# a.show() child methods are not accessible through parent

b = Bike(2, 300)
b.show()
b.info() #parnet methods are accessible through child