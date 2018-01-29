# * це по типу varargs. Означає, що наш метод приймає нуль і більше аргументів. Насправді *args це кортеж
def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()


# **, по типу, як *, тільки він є словником(dict)
def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


# приймає будь-які вхідні дані: список аргументів, колекції пар ключ/значення, чи їх комбінацію
def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()


myfunc(10)
myfunc()
myfunc(10, 20, 30, 40, 50)

values = [1, 2, 3, 4, 5]
myfunc(values)
# говоримо інтерпретатору розгорнути список, щоб кожен його елемент оброблювався, як окремий аргумент
myfunc(*values)  # типу ось так myfunc(1, 2, 3, 4, 5)

# ================================================================
myfunc2(a=10, b=20)  # a->10 b->20
myfunc2()
myfunc2(a=10, b=20, c=30, d=40, e=50, f=60)  # e->50 c->30 b->20 d->40 a->10 f->60

dbconfig = {'host': '127.0.0.1', 'user': 'vsearch', 'password': 'vsearchpasswd', 'database': 'vsearchlogDB', }
# говоримо інтерпретатору розгорнути словник, щоб кожен його елемент оброблювався, як окремий аргумент
myfunc2(**dbconfig)  # myfunc2(host='127.0.0.1', user='vsearch', ...)
# ================================================================
myfunc3()
myfunc3(1, 2, 3)                    # 1 2 3
myfunc3(a=10, b=20, c=30)           # b->20 c->30 a->10
myfunc3(1, 2, 3, a=10, b=20, c=30)  # 1 2 3 b->20 c->30 a->10






