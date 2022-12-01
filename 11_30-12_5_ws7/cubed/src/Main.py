import math

filename = input()
f = open(filename, 'r')

seed = int(f.readline())
import random
random.seed(seed)

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

first_number = int(f.readline())
second_number = int(f.readline())

if (first_number < 0 or first_number > second_number):
    print("INVALID INPUT")
    exit()

repeat = random.randint(15, 50)

print(first_number)
print(second_number)

new_number = 0

for _ in range(repeat):

    if _ % 3 == 0:
        new_number = (2 * first_number) - second_number

    elif _ % 3 == 1:
        new_number = first_number + second_number

    elif _ % 3 == 2:
        new_number = second_number ** 3
    new_number = int(new_number)

    first_number, second_number = second_number, new_number
    print(new_number)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE