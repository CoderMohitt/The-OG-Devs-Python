import math

class Programmer:
    def __init__(self, n, p):
        self.name = n
        self.position = p

    def show(self):
        print(f'name is {self.name} and positon is {self.position}')

himanshu = Programmer('Himanshu', 'SDE')
# print(himanshu.name)
# print(himanshu.position)
# himanshu.show()

saurabh = Programmer('Saurabh', 'Hacker')
# print(saurabh.name)
# print(saurabh.position)
# saurabh.show()

#4 -> 16, 64, 2 



class Calculator:
    def __init__(self, number):
        self.number = number

    def greet(fx):
        def mfx(self):
            print('hello')
            fx(self)
            print('thanks')

        return mfx    

    @greet
    def calculate_square(self):
        print(f'The Square is : {self.number * self.number}')
    
    @greet
    def calculate_cube(self):
        print(f'The Cube is : {self.number * self.number * self.number}')

    def calculate_root(self):
        print(f'The Root is : {math.sqrt(self.number)}')


# n = int(input('Enter a number : '))
square = Calculator(16)
# square.calculate_square()
square.calculate_cube()
# square.calculate_root()

class Demo:
    a = 10

# obj = Demo()
# obj.a = 20
# print(obj.a)

# obj1 = Demo()
# print(obj1.a)