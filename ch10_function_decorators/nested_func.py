def outer():
    def inner():
        print('This is inner.')

    print('This is outer, invoking inner.')
    # Функцію inner можно викликати лише з тіла функції outer, тому що inner знаходиться в області видимості outer
    inner()


outer()
