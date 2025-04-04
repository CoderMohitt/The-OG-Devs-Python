# l1 = [1, 1, 1, 3]

s = set()
# print(type(s))

s.add(1)
s.add(2)
# print(s[1])

s2 = {1, 2, 3, 4, 5}
# print(type(s2))

# print(len(s2))

# print(s2)

# s2.remove(2)
# s2.pop()

s2.clear()

# print(s2)

s1 = {1, 2, 3, 5}
s2 = {2, 4, 5, 6}

#{1, 2, 3, 4, 5, 6}

print(s1.intersection(s2))
print(s1.union(s2))