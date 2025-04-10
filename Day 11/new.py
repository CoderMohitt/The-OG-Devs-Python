# for i in range(1, 4):
#     print('*' * i)

i = 10

# while i > 0:
#     print(i * 5)
#     i = i - 1

# for i in range(10, 0, -1):
#     print(i * 4)

def greet():
    print('hello')
    print('user')

# greet() #function call
# greet()

# def greetUser():
#     print('good day')

# greetUser()

# def add(x, y, z): #function with arguments
#     print(x + y + z)

# a = int(input('Enter the value for a : '))
# b = int(input('Enter the value for b : '))
# c = int(input('Enter the value for c : '))

# add(a, b, c)

# name = 'mohit'

# def greetUser(name):
#     a = 'hello ' + name
#     return a

# result = greetUser('chandni')
# print(result)

# def add(x = 10, y = 10):
    
#     return x + y

# print(add(20, 20))

def helloUser(name = 'stranger'):
    return 'hello ' + name

print(helloUser('rohit'))