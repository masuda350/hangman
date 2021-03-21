index = float(input())

print(
    'Analytic' if index < 2 else
    'Synthetic' if index <= 3 else
    'Polysynthetic'
)
