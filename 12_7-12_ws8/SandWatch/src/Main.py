import random

filename = input()
fh = open(filename, 'r')
random.seed(20)

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


first_number = int(fh.readline())
second_number = int(fh.readline())

if first_number < 0:
    print("INVALID INPUT")
    exit()

if second_number < 0:
    print("INVALID INPUT")
    exit()

repeat = random.randint(first_number, second_number)

n = repeat
i = 0
while i <= n - 1:
    j = 0
    while j < i:
        # display space
        print('', end= ' ')
        j += 1
    k = i
    while k <= n - 1:
        print('*', end= ' ')
        k += 1
    print()
    i += 1

i = n - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end= ' ')
        j += 1
    k = i
    while k <=  n - 1:
        print('*', end= ' ')
        k += 1
    print('')
    i -= 1
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

