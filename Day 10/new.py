# for i in range(1, 11):
#     print(i * 5)

i = 1

# while i < 11:
#     print(5 * i)
#     i = i + 1

l1 = ['rajat', 'rahul', 'karuna', 'jyoti', 'ankita']

# for item in l1:
#     if(item.startswith('r')):
#         print('welcome', item)
#     else:
#         print('not welcome',item)


# for i in range(2, n): # 2,3,4,5,6,7,8,9, 10
#     if(n % i == 0): #11 % 2 == 0
#         print('not prime')
#         break
#     else:
#         print('prime')
#         break

#prime number -> 1, self -> 3 

n = 5 #1 + 2 + 3 + 4 + 5 = 15
sum = 0
i = 1

while i <= n:
    sum = sum + i 
    i = i + 1

'''
1st round -> i = 1
1 <= 5:
    sum = 0 + 1 = 1
    i = 2

2nd round -> i = 2
2 <= 5:
    sum = 1 + 2 = 3
    i = 3

3rd round -> i = 3
3 <= 5:
    sum = 3 + 3 = 6
    i = 4

4th round -> i = 4
4 <= 5:
    sum = 6 + 4 = 10
    i  = 5

5th round -> i = 5
5 <= 5:
    sum = 10 + 5 = 15
    i = 6

6th round -> i = 6
6 <= 5: 
'''

# print(sum) 

# 5! = 5 * 4 * 3 * 2 * 1 = 120
n = 3
fact = 1

for i in range(1, n + 1):
    fact = fact * i

# print(fact)

'''
1st round-> i = 1
fact = 1 * 1 = 1

2nd round -> 2
fact = 1 * 2 = 2

3rd round -> 3
fact = 2 * 3 = 6

4th round -> 
'''

# for i in range(1, 10):
#     print(i)

for i in range(3):
    print(' ' * (3 - i - 1), end='')

    print('*' * (2 * i + 1))

rows = 10

for i in range(rows):
    print(' ' * (rows - i - 1), end='')
    print('*' * (2 * i + 1))

# print('nit' * 4)

print('hello', end='')
print('world')
