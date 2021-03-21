offset = int(input())
reference = 10.5
time = reference + offset

print(
    'Wednesday' if time >= 24 else
    'Tuesday' if time >= 0 else 'Monday'
)

# Another solution 1
Monday = [-11, -12]
Wednesday = [+14]

if offset in Monday:
    print("Monday")
elif offset in Wednesday:
    print("Wednesday")
else:
    print("Tuesday")
