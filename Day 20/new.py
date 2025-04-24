'''
operator overloading -> 

print(2 + 2)
print('nit' + 'institute')

#doglapan of plus operator 

print(2 * 4)
print('nit' * 8)

#doglapan of *

'''
#2i + 3j + 4k
#3i + 5j + 8k
#5i + 8j + 12k

'''
__methodname__ magic method ya phir dunder methods
'''

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return (f'{self.i}i + {self.j}j + {self.k}k')
    
    def __add__(self, other):
        return f'{self.i + other.i}i + {self.j + other.j}j + {self.k + other.k}k'

a = Vector(4, 2, 8)
print(a)

b = Vector(5, 7, 4)
print(b)

print(a + b)
#doglapan but defined doglapan / + operator overloaded

'''
a + b
self            other
a                  b
self.i = 4   +  other.i / b.i = 5 = 9
self.j = 2   +   other.j / b.j = 7 = 9
self.k = 8   +   other.k / b.k = 4 = 12


'''