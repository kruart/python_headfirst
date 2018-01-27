class Person:
    name = "Tom"

    # всі класи мають конструктор за замовчуванням, однак тут ми визначаємо свій власний конст.
    def __init__(self, name='Anonymous'):
        self.name = name  # встановлюєм ім'я

    def display_info(self):
        print("Привіт, мене звуть", self.name)


person1 = Person("Tom")
person1.display_info()  # Привіт, мене звуть Tom
person2 = Person("Sam")
person2.display_info()  # Привіт, мене звуть Sam
person3 = Person()
person3.display_info()  # Привіт, мене звуть Anonymous


