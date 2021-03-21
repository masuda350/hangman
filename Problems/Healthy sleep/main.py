min_sleep = int(input())
max_sleep = int(input())
ann_sleep = int(input())

print(
    'Deficiency' if ann_sleep < min_sleep else
    'Excess' if ann_sleep > max_sleep else
    'Normal'
)
