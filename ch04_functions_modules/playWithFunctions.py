# function with param
def say_hello(name):
    print("Hello,", name)


say_hello("Tom")
say_hello("Bob")
say_hello("Alice")


# default value
def say_hello(name="World"):
    print("Hello,", name)


say_hello()
say_hello("Moon")


# function 2 params with different types
def display_info(name, age):
    print("Name:", name, "\t", "Age:", age)


display_info("Tom", 22)
display_info(age=40, name='Alex')   # named params


# function with return
def exchange(usd_rate, money):
    result = round(money/usd_rate, 2)
    return result


result1 = exchange(60, 30000)
print(result1)
print(exchange(57, 30000))


# In Python, a function can return multiple values at once
def create_default_user():
    name = "Kevin"
    age = 33
    return name, age


user_name, user_age = create_default_user()
print("Name:", user_name, "\t Age:", user_age)