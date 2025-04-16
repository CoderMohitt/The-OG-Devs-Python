class Person:
    name = 'mansi'
    occ = 'sde'

    def info(self):
        print(f'name is {self.name} and occupation is {self.occ}')

mansi = Person() #mansi is a object of class Person
print(mansi.name)
print(mansi.occ)

#objectname.attributename

# print(name)
# print(occ)

mansi.info()

# def add(a, b):
#     print(a + b)

# add(10, 20)

himanshu = Person()
himanshu.name = 'himanshu'
print(himanshu.name)
himanshu.occ = 'software dev'
print(himanshu.occ)

himanshu.info()

paras = Person()
print(paras.name)