import statistics

# put your python code here
a = int(input())
b = int(input())

divider_3 = [i for i in range(a, b + 1) if not i % 3]
print(sum(divider_3) / len(divider_3))

# Another solution 1
print(statistics.mean(divider_3))

# Another solution 2
a = a - (a % -3)  # first number which is multiple of 3
r = range(a, b + 1, 3)
print(sum(r) / len(r))

# Another solution 3
total = 0
count = 0

for i in range(a, b + 1):
    if not i % 3:
        total += i
        count += 1

print(total / count)

# Another solution 4
a, b = map(int, [input(), input()])

shift = 3 - a % 3 if a % 3 else 0
valid = range(a + shift, b + 1, 3)

print(sum(valid) / len(valid))
