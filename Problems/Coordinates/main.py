x = float(input())
y = float(input())

if x == 0 and y == 0:
    print("It's the origin!")
elif x == 0 or y == 0:
    print("One of the coordinates is equal to zero!")
else:
    if x > 0 and y > 0:
        print("I")
    elif x > 0:
        print("IV")
    elif y > 0:
        print("II")
    else:
        print("III")

    # Another solution 1
    # if x > 0:
    #     q = "I" + "V" * (y < 0)
    # else:
    #     q = "II" + "I" * (y < 0)
    # print(q)

    # Another solution 2
    # if x > 0:
    #     print("I" if y > 0 else "IV")
    # else:
    #     print("II" if y > 0 else "III")

    # Another solution 3
#     if x > 0:
#         quad = "I" if y > 0 else "IV"
#     else:
#         quad = "II" if y > 0 else "III"
#
# print(quad)