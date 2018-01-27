class Person:
    def __init__(self, name, age):
        self.__name = name  # встановлюєм ім'я
        self.__age = age  # встановлюєм вік

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимий вік")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print("Ім'я:", self.__name, "\tВік:", self.__age)


# Employee наслідується від Person
class Employee(Person):

    def details(self, company):
        # print(self.__name, "працює в компанії", company) # так не можна, self.__name - приватний атрибут
        print(self.name, "працює в компанії", company)


tom = Employee('Tom', 23)
tom.details('Google')
tom.age = 33
tom.display_info()
