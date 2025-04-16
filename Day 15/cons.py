class Person:
    def __init__(self, n, o): #constructor automatically called
        self.name = n
        self.occ = o

    def info(self):
        print(f'name is {self.name} and occupation is {self.occ}')


pooja = Person('pooja', 'sde') 
# print(pooja.name)
# print(pooja.occ)
# pooja.info()

aman = Person('aman', 'software dev')
# print(aman.name)
# print(aman.occ)
# aman.info()

# payal = Person()

class Railway:
    def __init__(self, name, stno, mobno):
        self.name = name
        self.stno = stno
        self.mobno = mobno

    def info(self):
        print(f'name : {self.name} \nstation no. : {self.stno} \nmobile no. : {self.mobno}')

rahul = Railway('Rahul', 10, '1234656')
rahul.info()

aman = Railway('Aman', 4, 1546872)
aman.info()