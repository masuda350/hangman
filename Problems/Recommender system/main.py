age = int(input())

if age > 60:
    print("Breakfast at Tiffany's")
elif age > 40:
    print("Pulp Fiction")
elif age > 25:
    print("Matrix")
elif age > 16:
    print("Trainspotting")
else:
    print("Lion King")

# Another solution 1
rec = {
    "Lion King": range(0, 17),
    "Trainspotting": range(17, 26),
    "Matrix": range(26, 41),
    "Pulp Fiction": range(41, 61),
    "Breakfast at Tiffany's": range(61, 150)
}
age = int(input())
for title, number in rec.items():
    if age in number:
        print(title)

# Another solution 2
print(
    "Lion King" if age <= 16 else
    "Trainspotting" if age <= 25 else
    "Matrix" if age <= 40 else
    "Pulp Fiction" if age <= 60 else
    "Breakfast at Tiffany's"
)
