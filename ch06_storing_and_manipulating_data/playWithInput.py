todos = open('todos.txt', 'a')

print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)

todos.close()


# read from file in loop
tasks = open('todos.txt')   # read - default mode
for ch in tasks:
    print(ch, end='')

tasks.close()


# write()
try:
    somefile = open("hello.txt", "w")   # відкриваємо файл
    try:
        somefile.write("hello world")   # пишемо в нього
    except Exception as e:
        print(e)
    finally:
        somefile.close()                # закриваємо
except Exception as ex:
    print(ex)


# the same in more short way: construction with(auto closeable file, even exception would be thrown)
with open("hello.txt", "w") as somefile:
    somefile.write("hello world")


with open('todos.txt') as somefile:
    content = somefile.read()

    print('=====================')
    print(content)