percentage = int(input()) / int(input()) * 100

if 90 <= percentage <= 100:
    print('A')
elif 80 <= percentage < 90:
    print('B')
elif 70 <= percentage < 80:
    print('C')
elif 60 <= percentage < 70:
    print('D')
else:
    print('F')

# Another solution 1
score = int(input())
max_score = int(input())

grade = 'FFFFFFDCBAA'[int(score / max_score * 10)]

print(grade)

# Another solution 2
grades = 'FDCBA'
percentage = 100 * int(input()) // int(input())
print(grades[max(0, min(percentage, 99) // 10 - 5)])

# Another solution 3
grade = float(input()) / float(input())

print(
    'A' if grade >= 0.9 else
    'B' if grade >= 0.8 else
    'C' if grade >= 0.7 else
    'D' if grade >= 0.6 else
    'F'
)