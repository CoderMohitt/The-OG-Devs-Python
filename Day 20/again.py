class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k'
    
    def __add__(self, other): #self ke andar + se pahle wala object and other ke andar + ke bad wala object
        return Vector(
            self.i + other.i,
            self.j + other.j,
            self.k + other.k
        )

a = Vector(4, 5, 6)
print(a) #jab mai object ko print karta hun tab str method call hota hai? yes

b = Vector(7, 8, 9)
print(b) #kya hoga

c = Vector(1, 2, 3)
print(c)
 
print(a + b + c) #(a + b) + c