#recursion -> calling the same function inside the function

# def greet():
#     print('hello')
#     greet()

# def sayHello(name):
1#     print('hello ', name)

# greet()

'''
factorial

5! = 5 * 4!
4! = 4 * 3!

factorial(n) = n * factorial(n - 1)
factorial(5) = 5 * factorial(4)

3! = 3 * 2 * 1
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# print(factorial(5))

'''
fact(5) = 5 * 4 * 3 * 2 * 1 = 120

fact(5) = 5 * fact(4)
fact(5) = 5 * 4 * fact(3)
fact(5) = 5 * 4 * 3 * fact(2)
fact(5) = 5 * 4 * 3 * 2 * fact(1)
fact(5) = 5 * 4 * 3 * 2 * 1 = 120
'''

#0  1 1 2 3 5 8
#n = 5 ans = 3

def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(5 - 1))
print(fib(1))
