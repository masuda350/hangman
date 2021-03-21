for num in range(1, 101):
    print(
        'FizzBuzz' if num % 3 == 0 and num % 5 == 0 else
        'Fizz' if num % 3 == 0 else
        'Buzz' if num % 5 == 0 else
        num
    )

# Another solution 1
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)

# Another solution 2
for i in range(1, 101):
    print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)
