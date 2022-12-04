import random

filename = input()
f = open(filename, 'r')
seed = int(f.readline())
random.seed(seed)

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

first_number = int(f.readline())
second_number = int(f.readline())

if (first_number < 0 or first_number > second_number):
    print("INVALID INPUT")
    exit()

repeat = random.randint(5, 20)

print(first_number)
print(second_number)

for i in range(repeat):

    if i % 4 == 0:
        new_number = (3 * first_number) + (4 * second_number)

    elif i % 4 == 1:
        new_number = 4 * first_number + (second_number ** (first_number%3))

    elif i % 4 == 2:
        new_number = (2 * first_number + 2 * second_number) % 500

    elif i % 4 == 3:
        new_number = (first_number% 100) + (second_number%100)

    first_number, second_number = second_number, new_number
    print(new_number)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

