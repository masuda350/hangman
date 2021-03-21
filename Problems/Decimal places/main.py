num = float(input())
dec = input()

print('{0:.{1}f}'.format(num, dec))

print(f'{num:.{dec}f}')

print(f'{float(input()):.{input()}f}')

print('%.*f' % (int(dec), num))

# d is to convert dec String to integer
print(f'%d.{dec}f' % num)
