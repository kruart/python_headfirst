
def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After:  ', arg)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After:  ', arg)


num = 10
double(num)
print(num)      # didn't change
saying = 'Yeah'
double(saying)
print(saying)   # didn't change
numbers = [32, 64, 128, 256]
double(numbers)
print(numbers)  # didn't change

print('===================')
change(numbers)
print(numbers)
