class Railway:
    name = 'mohit'
    stno = 4
    foodFacility = True

    def info(self):
        print(f'name of ticket holder is {self.name} and station number is {self.stno} and they have foodFacility : {self.foodFacility}')

mansi = Railway()
mansi.name = 'mansi'
mansi.stno = 10
mansi.foodFacility = False

print(mansi.name)
print(mansi.stno)
print(mansi.foodFacility)

mansi.info()