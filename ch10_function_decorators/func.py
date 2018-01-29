# функція apply приймає об'єкт функції в аргументі. Використання імені func, - загальноприйнята конвенція
def apply(func: object, value: object) -> object:
    return func(value)      # результат виклику func() повертається з функції apply()


def print_my_name(value: str) -> None:
    print('My name is', value)


apply(print_my_name, 'Arthur')  # My name is Arthur
apply(print, 'Arthur')          # Arthur
print(apply(type, 42))          # <class 'int'>
print(apply(type, apply))       # <class 'function'>
