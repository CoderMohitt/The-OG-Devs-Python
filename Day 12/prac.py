def greatest_of_three(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c
    
# print(greatest_of_three(100, 20, 30))

def celcius_to_farenheit(value):
    return (value * 9 / 5) + 32

# print(celcius_to_farenheit(100))

# print('hello', end='')
# print('world')

#5 -> 1 + 2 + 3 + 4 + 5 = 15
#5 -> 1 + sum(4)

def sum_n_natural(n):
    if n <= 1:
        return 1
    return n + sum_n_natural(n - 1)

# print(sum_n_natural(10))


def print_pattern(n):
    for i in range(n, 0, -1):
        print('*' * i)

# print_pattern(6)

# for i in range(3, 0, -1):
#     print(i)

def inch_to_cm(value):
    return value * 2.54

# print(inch_to_cm(1))

a = '   mohit    '

# print(a)
# print(a.strip())

def table(n):
    for i in range(1, 11):
        print(n * i)

table(41)