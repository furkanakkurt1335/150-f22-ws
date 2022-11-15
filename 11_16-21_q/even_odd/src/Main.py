# Read the file
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
f = open(filename, 'r')
n = int(f.readline())
t = int(f.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
def even_odd(number, turn):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if turn != 0:
        if number % 2 == 0:
            number = ((number % 10)*10)+(number//10)
            turn += -1
            return even_odd(number, turn)
        else:
            number += 11
            turn += -1
            return even_odd(number, turn)
    else:
        return number, 0

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

# You need to call the `even_odd` function below
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

final, turn = even_odd(n, t)
print(final)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
