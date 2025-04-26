'''
govt job form -> vasudha, ankita, rajat, paras

hard copy form -> same -> class
details -> unique -> object

class is a blueprint for object
'''

class GovtForm:
    #class ke andar variable bhi banaye ja sakte hai or functions bhi bnaye ja sakte hai 
    #variable -> attribute
    #functions -> methods

    #name, category, age, dob

    #attributes init karne ke liye kya use hota hai?

    def __init__(self, name, category, age, dob): #self ke andar automatically object pass hota hai 
        self.n = name
        self.c = category
        self.a = age
        self.d = dob

    def __str__(self): #jab bhi object ko print karte hai to __str__ method call hota hai, pahle defined nahi tha isliye memory location aa rahi thi lekin ab defined hai isliye print hoga ye sab
        return f'name : {self.n}, category : {self.c}, age : {self.a}, DOB : {self.d}'

vasudha = GovtForm('Vasudha', 'General', 20, "20-5-2006") #constructor called
# print(vasudha)

rajat = GovtForm('Rajat', 'General', 25, "20-05-2000")
# print(rajat)

# paras = GovtForm()



#name : rajat, age : 20
# print('name :', name, 'age :', age)
# print(f'name : {name}, age : {age}')



#gta -> main char
#       npc - > non playble character
#walk, run, drive -> npc
#walk, run, drive, shooting -> main char

#parent -> child

class NPC:
    def __init__(self, walk, run, drive):
        self.walk = walk
        self.run = run
        self.drive = drive

    def show(self):
        print(f'this player can walk : {self.walk}, can run : {self.run}, can drive : {self.drive}')

class MainChar(NPC):
    def __init__(self, walk, run, drive, shoot):
        super().__init__(walk, run, drive)
        self.shoot = shoot

    def show(self):
        super().show()
        print(f'can shoot : {self.shoot}')

a = NPC('Yes', 'Yes', 'Yes')
a.show()

b = MainChar('Yes', 'Yes', 'Yes', 'Yes')
b.show()