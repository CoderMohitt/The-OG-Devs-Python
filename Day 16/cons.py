class Railway:
    def __init__(self, n, s): #constructor
        self.name = n
        self.stno = s
    
    def show(self):
        print(f'name is {self.name} and station number is {self.stno}')

# a = Railway('Mansi', 4)
# print(a.name)
# print(a.stno)
# a.show()

# b = Railway('Himanshu', 10)
# print(b.name)
# print(b.stno)
# b.show()

def greet(fx):
    def mfx(*args):
        print('welcome')
        fx(*args)
        print('thanks')
    return mfx

@greet
def hello():
    print('hello world')

hello()

@greet
def add(a, b):
    print(a + b)

add(1, 5)
# def mul(a, b):
#     print(a * b)


#welcome to my function
#work
#thanks for using the function

#decorators -> functions that modifies other functions

# def some(*a):
#     print(a)

# some(1, 2, 3, 4, 5, 6, 7)