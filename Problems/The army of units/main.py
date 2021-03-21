unit = int(input())
if unit < 1:
    print('no army')
elif 1 <= unit < 10:
    print('few')
elif 10 <= unit < 50:
    print('pack')
elif 50 <= unit < 500:
    print('horde')
elif 500 <= unit < 1000:
    print('swarm')
else:
    print('legion')

# Another solution 1
categories = {
    1: "few",
    10: "pack",
    50: "horde",
    500: "swarm",
    1000: "legion",
}

category = "no army"

for key, value in categories.items():
    if unit >= key:
        category = value

print(category)

# Another solution 2
for key in categories:
    if key is True:
        print(categories.get(key))
