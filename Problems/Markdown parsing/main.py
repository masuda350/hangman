text = input()

print(text.lstrip('*_~`').rstrip('*_~`'))

# Another solution 1
print(text.strip('*_~`'))
