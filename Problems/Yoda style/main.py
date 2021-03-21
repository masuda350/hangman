import random

# your sentence is assigned to the variable
sentence = input().split()

# write your python code below
random.seed(43)
random.shuffle(sentence)

# Another solution 1
random.shuffle(sentence, random.seed(43))

# shows the message
print(' '.join(sentence))