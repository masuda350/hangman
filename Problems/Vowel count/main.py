string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0

for vowel in vowels:
    count += string.count(vowel)

print(count)

# Another solution 1
print(sum(letter in vowels for letter in string))

# Another solution 2
print(len([letter for letter in string if letter in vowels]))

# Another solution 3
print(sum(1 for letter in string if letter in vowels))