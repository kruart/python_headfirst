# більш елегантний спосіб визначення властивостей
class Person:
    # для створення приватного атрибуту на початку його найменування ставиться подвійний прочерк: self.__name.
    # до такого атрибуту ми зможемо звернутися тільки з того ж класу. А зовні - лише через методи.
    def __init__(self, name, age):
        self.__name = name  # встановлюєм ім'я
        self.__age = age  # встановлюєм вік

    # для створення властивості-геттера над властивістю ставиться анотація @property
    @property
    def age(self):
        return self.__age

    # для створення властивості-сетера над властивістю встановлюється анотація ім'я_свойства_геттера.setter
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    # для створення властивості-геттера над властивістю ставиться анотація @property
    @property
    def name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


# після цього, що до геттера, що до сетера, ми звертаємося через вираз tom.age.
tom = Person("Tom", 23)

tom.display_info()   # Ім'я: Tom  Вік: 23
tom.age = -3486      # Недопустимий вік
print(tom.age)       # 23
tom.age = 36
tom.display_info()   # Ім'я: Tom  Вік: 36
