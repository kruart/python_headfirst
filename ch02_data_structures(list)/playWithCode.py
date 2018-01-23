# remove
nums = [1, 2, 3, 4]
nums.remove(2)
print(nums)
# nums.remove(2)  # throw ValueError

# pop
cars = ['Fiat', 'KIA', 'Tesla', 'Toyota', 'Nissan']
cars.pop()  # remove and return last element in list
kia = cars.pop(1)  # remove and return item at index
print(kia)
print(cars)

# extend
nums.extend([11, 12, 13])
print(nums)

# insert
nums.insert(3, 999)
print(nums)

letters = list("Don't panic")
print(letters[0])        # перший індекс
print(letters[-1])       # останній індекс
print(letters[0:10:3])   # кожна третя літера до індексу 10
print(letters[3:])       # пропустити перші три літери
print(letters[:10])      # всі літери до індексу 10
print(letters[::2])      # кожна друга літера
print(''.join(letters[0:5]))      # panic
print(''.join(letters[::-1]))
