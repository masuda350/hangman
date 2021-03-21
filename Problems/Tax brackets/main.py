import sys

income = int(input())

tax_bracket = {
    0: range(0, 15528),
    15: range(15528, 42708),
    25: range(42708, 132407),
    28: range(132407, sys.maxsize)
}

for tax, salary in tax_bracket.items():
    if income in salary:
        calculated_tax = income * tax / 100
        print('The tax for {} is {}%. That is {:.0f} dollars!'.format(income, tax, calculated_tax))

# Another solution 1
tax_bracket = {
    132407: 28,
    42708: 25,
    15528: 15,
    0: 0
}

for salary in tax_bracket:
    if income >= salary:
        calculated_tax = income * tax_bracket[salary] / 100
        print(f'The tax for {income} is {tax_bracket[salary]}%. That is {calculated_tax:.0f} dollars!')
        break

# Another solution 2
tax = 0

if income in range(15_528, 42_708):
    tax = 15
elif income in range(42_708, 132_407):
    tax = 25
elif income >= 132_407:
    tax = 28


calculated_tax = income * tax / 100

print(f"The tax for {income} is {tax}%. That is {calculated_tax:.0f} dollars!")