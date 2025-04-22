#access modifiers -> public, private, protected attributes

#public -> accessible inside the class as well as outside the class

#private -> cant be accessed outside

#protected -> accessible inside the class and in the child classes

class Vehicle:
    name = 'ferrari' # public attribute 
    __model = 's3' # private attribute / name mangling
    _speed = 300 # protected attribute

a = Vehicle()
print(a.name)
print(a._Vehicle__model) # indirectly accessed
# print(a.__dir__())
print(a._speed)