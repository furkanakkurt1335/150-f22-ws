import random

filename = input()
fh = open(filename, 'r')
random.seed(12)

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

first_number = int(fh.readline())
second_number = int(fh.readline())

if first_number < 0:
    print("INVALID INPUT")
    exit()

if second_number < 0:
    print("INVALID INPUT")
    exit()

side = random.randint(first_number, second_number)

for i in range(side):
    if i == side - 1:
        print('*', end='')
    else:
        print('*', end=' ')
print()
for i in range(side-2):
    print('*' + ' '*(2*(side-1)-1) + '*')
for i in range(side):
    if i == side - 1:
        print('*', end='')
    else:
        print('*', end=' ')

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

