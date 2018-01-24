vowels1 = ['a', 'e', 'i', 'o', 'u']
print(vowels1)          # ['a', 'e', 'i', 'o', 'u']
print(type(vowels1))    # class list

vowels2 = ('a', 'e', 'i', 'o', 'u')
print(vowels2)          # ('a', 'e', 'i', 'o', 'u')
print(type(vowels2))    # class tuple


# vowels2[2] = 'I' # tuple is immutable type, we can't change tuple

user = ("User", 23)  # для створення кортежу використовуються круглі дужки, в які поміщаються його значення, розділені комами
user1 = "User1", 23    # також для визначення кортежу ми можемо просто перерахувати значення через кому без застосування дужок
user2 = ("User2",)     # якщо раптом кортеж складається з одного елемента, то після нього необхідно поставити кому

users = ("Tom", "Bob", "Sam", "Kate")
users_tuple = tuple(users)      # для створення кортежу зі списку можна передати список в функцію tuple(), яка поверне кортеж
print(users[0])                 # звернення до елементів кортежу відбувається по індексу
print(users[1:4])               # ("Bob", "Sam", "Kate")

# users[1] = "Tim"                # але так як кортеж - незмінний тип (immutable), то ми не зможемо змінити його елементи

# при необхідності ми можемо розкласти кортеж на окремі змінні:
user3 = ("User3", 22, False)
name, age, isMarried = user3
print(name)         # Tom
print(age)          # 22
print(isMarried)    # False


# особливо зручно використовувати кортежі, коли необхідно повернути з функції відразу кілька значень. Коли функція повертає кілька значень, фактично вона повертає в кортеж:
def get_user():
    name = "User5"
    age = 26
    is_married = False
    return name, age, is_married


user5 = get_user()
print(type(user5))  # <class 'tuple'>
print(user5[0])     # Tom
print(user5[1])     # 22
print(user5[2])     # False
# ==============
len(users)          # за допомогою вбудованої функції len() можна отримати довжину кортежу

for item in user5:  # ітерація по кортежу, так само, як в list, set and dict
    print(item)

# ===================Складні кортежі. Один кортеж може містити інші кортежі у вигляді елементів. наприклад:
countries = (
    ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2), ("Marsel", 1.6)))
)

for country in countries:
    countryName, countryPopulation, cities = country
    print("\nCountry: {}  population: {}".format(countryName, countryPopulation))
    for city in cities:
        cityName, cityPopulation = city
        print("City: {}  population: {}".format(cityName, cityPopulation))