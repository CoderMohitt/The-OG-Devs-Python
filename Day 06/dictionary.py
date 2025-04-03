'''
word: meaning
key: value
'''

a = {
    'paras': 100,
    'rajat': 56,
    'paras': 45,
    'students': [10, 20, 30]
}
# print(type(a))
# print(a)

# print(a)

info = {
    'name': 'mohit',
    'from': 'India',
    'marks': [10, 20, 30]
}

a = {
    'name': 'rahul',
    'branch': 'it',
    'age': 20
}

b = {
    'name': 'mansi',
    'branch': 'it',
    'age': 20
}

b.update({'habit': 'scrolling'})

# print(b)

print(b.get('name'))

# print(a.items())

# print(a.keys())
a.update({'friend' : 'rajat'})
# print(a)

# print(info.items())

# [(key, value), (key, value),(key, value)]