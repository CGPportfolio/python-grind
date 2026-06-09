import random

size = int(input('Enter the tree size: '))

for row_num in range(1, size + 1):
    row = ''
    for i in range(row_num * 2 - 1):
        if random.randint(1, 4) == 1:
            row += 'o'
        else:
            row += '^'
    print(' ' * (size - row_num) + row)

for i in range(2):
    print(' ' * (size - 1) + '#')
