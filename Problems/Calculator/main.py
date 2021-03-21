# put your python code here
first = float(input())
second = float(input())
arithmetic = input()

if arithmetic in '+':
    print(first + second)
elif arithmetic in '-':
    print(first - second)
elif arithmetic in '*':
    print(first * second)
elif arithmetic in 'pow':
    print(first ** second)
elif second == 0:
    print('Division by 0!')
elif arithmetic in 'mod':
    print(int(first % second))
elif arithmetic in '/':
    print(first / second)
elif arithmetic in 'div':
    print(int(first // second))

# Another solution 1
operation = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b,
    'mod': lambda a, b: a % b,
    'pow': lambda a, b: a ** b,
    'div': lambda a, b: a // b
}

try:
    print(operation[arithmetic](first, second))
except ZeroDivisionError:
    print('Division by 0!')
