import random

filename = input()
fh = open(filename, 'r')
seed = int(fh.readline())
random.seed(seed)

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

first_number = int(fh.readline())
second_number = int(fh.readline())

if (first_number < 0 or first_number > second_number):
    print("INVALID INPUT")
    exit()

repeat = random.randint(5, 10)

print(first_number)
print(second_number)

for _ in range(repeat):

    if _ % 3 == 0:
        new_number = 4 * first_number + second_number

    elif _ % 3 == 1:
        new_number = (7 * first_number + second_number) % 1000

    elif _ % 3 == 2:
        new_number = 3 * first_number + second_number

    first_number, second_number = second_number, new_number
    print(new_number)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
