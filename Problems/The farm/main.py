money = int(input())

items = {
    'sheep': 6769,
    'cow': 3848,
    'pig': 1296,
    'goat': 678,
    'chicken': 23
}

category = {'None': 0}

for item, price in items.items():
    if money >= price:
        category.clear()
        quantity = money // price
        if quantity == 1 or item.__contains__('sheep'):
            category[item] = quantity
        else:
            category[item + 's'] = quantity
        break

for item, quantity in category.items():
    print(None) if 'None' in category else print(quantity, item)

# Another solution 1
if money < items['chicken']:
    print(None)
else:
    for animal, cost in items.items():
        if money >= cost:
            quantity = money // cost
            output = animal + 's' if quantity > 1 and animal != 'sheep' else animal
            print(quantity, output)
            break

# Another solution 2
sheep = money // 6769
cow = money // 3848
pig = money // 1296
goat = money // 678
chicken = money // 23

if sheep:
    print(sheep, 'sheep')
elif cow:
    print(cow, 'cows' if cow > 1 else 'cow')
elif pig:
    print(pig, 'pigs' if pig > 1 else 'pig')
elif goat:
    print(goat, 'goats' if goat > 1 else 'goat')
elif chicken:
    print(chicken, 'chickens' if chicken > 1 else 'chicken')
else:
    print('None')
