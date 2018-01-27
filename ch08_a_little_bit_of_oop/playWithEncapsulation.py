class Person:
    # для створення приватного атрибуту на початку його найменування ставиться подвійний прочерк: self.__name.
    # до такого атрибуту ми зможемо звернутися тільки з того ж класу. А зовні - лише через методи.
    def __init__(self, name, age):
        self.__name = name  # встановлюєм ім'я
        self.__age = age  # встановлюєм вік

    def age(self, age) -> None:
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self) -> str:
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


tom = Person("Tom", 23)

tom.__age = 43      # Атрибут age не змінився
tom.display_info()  # Ім'я: Tom  Вік: 23
tom.set_age(-3486)  # Недопустимий вік
tom.set_age(25)
tom.display_info()  # Ім'я: Tom  Вік: 25
