snake_case = ''

for letter in input():
    if letter.isupper():
        snake_case += '_'
    snake_case += letter

print(snake_case.lower().lstrip('_'))

# # Another solution 1
# snake_case = ''
#
# for letter in input():
#     if letter.isupper() and snake_case:
#         snake_case += '_'
#     snake_case += letter
#
# print(snake_case.lower())
#
# # Another solution 2
# camelCase = input()
# snake_case = camelCase[0].lower()
#
# for letter in camelCase[1:]:
#     if letter.isupper():
#         snake_case += "_"
#     snake_case += letter.lower()
#
# print(snake_case)
#
# # Another solution 3
# camelCase = input()
#
# for letter in camelCase[1:]:
#     if letter.isupper():
#         camelCase = camelCase.replace(letter, ("_" + letter.lower()))
#
# print(camelCase.lower())
#
# # Another solution 3
# camelCase = input()
# print(camelCase[0].lower() + ''.join("_" + c.lower() if c.upper() == c else c for c in camelCase[1::]))
