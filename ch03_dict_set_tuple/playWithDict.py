# 1 way to declare dict
person3 = {'Name': 'Ford Prefect',
           'Gender': 'Male',
           'Occupation': 'Researcher',
           'Home Planet': 'Betelgeuse Seven'}
print(person3)

# 2 way to declare dict
d = dict(short='dict', long='dictionary')   # {'long': 'dictionary', 'short': 'dict'}
print(d)
d = dict([(1, 1), (2, 4)])
print(d)

# 3 way to declare dict
d = dict.fromkeys(['a', 'b'])       # {'a': None, 'b': None}
print(d)
d = dict.fromkeys(['a', 'b'], 100)  # {'a': 100, 'b': 100}
print(d)

# 4 way to declare dict
d = {a: a ** 2 for a in range(7)}   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
print(d)

print(person3['Name'])
person3['Age'] = 33
print(person3)