column = int(input())
row = int(input())

corners = 1, 8

if column in corners and row in corners:
    print(3)
elif column in corners or row in corners:
    print(5)
else:
    print(8)

# Another solution 1
column = 1 < int(input()) < 8
row = 1 < int(input()) < 8

print(
    8 if column and row
    else 5 if column ^ row
    else 3
)
