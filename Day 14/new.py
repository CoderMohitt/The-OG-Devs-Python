#procedural programming -> 

#object oriented programming -> classes and objects

#businessman 1
sales = 10000
profit = 3000
ad = 500
# rahul.sales(data)

#businessman 2
sales2 = 15000
profit2 = 5000
ad2 = 1000
# rajat.sales(data)

#gta -> gun, health(100 - 0)

#inheritance -> main player - npc(non playable char)

#main player -> npc

#npc -> run, walk, drive --> main player -> run, walk, drive, gun, helicopter

#what is class and what is object

#railway form -> class (template)
#rahul -> name, father name, station no -> object of railway form
#paras ->  name, father name, station no
#vasudha ->  name, father name, station no

class Person:
    name = 'rahul' #attributes
    occ = 'SDE'

    def info(self): #methods
        print(f'{self.name} is a {self.occ}')

rahul = Person()
rahul.info()

print(rahul.name)
# print(rahul.occ)

paras = Person()
paras.name = 'paras'
paras.occ = 'data scientist'

paras.info()

# print(paras.name)
# print(paras.occ)

vasudha = Person()
vasudha.name = 'vasudha'
vasudha.occ = 'hacker'
vasudha.info()

# print(vasudha.name)
# print(vasudha.occ)

# name = 'mohit'
# occ = 'SDE'

# print(name, 'is a', occ)
# print(f'{name} is a {occ}')

#mohit is a SDE

def add(a, b):
    print(a + b)

add(10, 5)