import re

text = input()

text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('!', '')
text = text.replace('?', '')

print(text.lower())

# Another solution 1
text = input().lower()
for char in ",.!?":
    text = text.replace(char, '')
print(text)

# Another solution 2
text = input()
for char in ["!", "?", ",", "."]:
    text = text.replace(char, "")
print(text.lower())

# Another solution 3
text = input().lower()
for letter in text:
    if letter in ",.!?":
        text = text.replace(letter, "")
print(text)

# Another solution 4
print(input().lower().replace(",", "").replace(".", "").replace("!", "").replace("?", ""))

# Another solution 5
print(re.sub("[,.!?]", "", input()).lower())
