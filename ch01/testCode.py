for number in range(5):
    print(number)
#####################################
b = list(range(1, 10, 2))
print(b)  # [1, 3, 5, 7, 9]

for number in [0, 1, 2, 3, 4]:
    print(number)

#####################################
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    if i == 6:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")

#####################################
i = 90
while i < 100:
    print(i)
    i = i + 1
#####################################
i = 0
while i < 10:
    if i == 3:
        i += 1
        continue

    print(i)
    if i == 5:
        break

    i += 1

