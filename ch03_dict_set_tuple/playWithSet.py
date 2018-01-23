users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users3 = users.union(users2)    # об'єднує дві множини і повертає нову множину
users4 = users.intersection(users2)     # дозволяє отримати тільки ті елементи, які є одночасно в обох множинах
users5 = users & users2    # Замість intersection ми могли б використ. операцію логічного множення. Результат той же
users6 = users.difference(users2)   # повертає ті елементи, які є в першій множині, але відсутні в другій.

print(users3)
print(users4)
print(users5)
print(users6)

# =======================================
usersN = {"Tom", "Bob", "Alice"}
superusers = {"Bob", "Sam", "Tom", "Greg", "Alice"}
# issubset дозволяє з'ясувати, чи є поточний множина підмножиною (тобто частиною) іншої множини
print(usersN.issubset(superusers))   # True
print(superusers.issubset(usersN))   # False
# issuperset, навпаки, повертає True, якщо поточна множина є надмножиною (тобто містить) для іншої множини
print(users.issuperset(superusers))   # False
print(superusers.issuperset(users))   # True

# =======================================
# Тип frozen set є видом множин, яку не може бути змінено. Для її створення використовується функція frozenset
# У функцію frozenset передається набір елементів - список, кортеж, інша множина.
# Такий тип frozen set має обмежений набір методів
users = frozenset({"Tom", "Bob", "Alice"})
