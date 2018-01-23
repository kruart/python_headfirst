vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)


print(len(found))
for vowel in found:
    print(vowel)