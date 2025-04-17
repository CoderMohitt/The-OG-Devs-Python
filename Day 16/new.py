#procedural programming

#object oriented programming -> classes and object

#rajat -> form -> name, station no.-> same -> details -> unique
#rahul -> form ->  name, station no. -> same -> details -> unique
#paras -> from ->  name, station no. -> same -> details -> unique

class Railway:
    #attributes -> variables
    name = 'rajat'
    stno = 10

    #methods -> functions
    def show(self):
        print(f'name is {self.name}')

a = Railway()
a.name = 'Paras'
print(a.name)
a.show()

b = Railway()
b.name = 'Rahul'
print(b.name)
b.show()

c = Railway()
c.name = 'Himanshu'
c.show()