class NPC:
    def __init__(self, run, walk, drive):
        self.run = run
        self.walk = walk
        self.drive = drive

    def details(self):
        print(f'this is a npc and can run : {self.run}, can walk : {self.walk}, can drive : {self.drive}')

class MainPlayer(NPC):
    def __init__(self, run, walk, drive, shoot):
        super().__init__(run, walk, drive)
        self.shoot = shoot

    def show(self):
        super().details()
        print(f'can shoot : {self.shoot}')

#npc -> mainplayer
a = NPC(True,True, True)
# a.details()

b = MainPlayer(True, True, True, True)
# b.show()

'''
types of inheritance -> 
1. single inheritance -> single parent single child
2. multiple inheritance -> two or more parents single child
3. multi level inheritance -> A -> B -> C
'''

#1. Single Inheritance

class Animal:
    def __init__(self, species):
        self.species = species

    def show(self):
        print(f'this is a animal and the species is {self.species}')

class Dog(Animal): #iske pas animal(parent) ke attributes and methods ka access hai
    def __init__(self, species, name):
        super().__init__(species) #apne parent ke constructor ko call karo
        self.name = name

    def info(self):
        super().show() #parent se show ko call karo
        print(f'name is {self.name}')

a = Dog('dog', 'Bruno')
# a.info()
#a.show() #child class se parent class ke method ko call kar diya

#2. Multiple -> 

class Employee:
    def __init__(self, id):
        self.id = id

    def show(self):
        print(f'this is a employee with id {self.id}')

class Dancer:
    def __init__(self, danceType):
        self.danceType = danceType

    def show(self):
        print(f'the dance type is {self.danceType}')

class DancerEmployee(Employee, Dancer): #danceremployee ke pas dancer or employee class ke mehtods and attributes hai 
    def __init__(self, id , danceType, talented):
        super().__init__(id)
        self.talented = talented
        self.danceType = danceType


d = DancerEmployee(420, 'hip hop', True)
#d.show() #papa ko jyda acha man rahe ho ya phir mummy ko

#mro -> method resolution order
# print(DancerEmployee.mro())

#3. multi level -> 

class Dadaji:
    def dada(self):
        print('ham hai dadaji')

class Pitaji(Dadaji):
    def pita(self):
        print('ham hai pitaji')

class Betaji(Pitaji):
    def beta(self):
        print('ham hai betaji')

a = Betaji()
a.beta()
a.pita()
a.dada()