# Read the file
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
f = open(filename, 'r')
n = int(f.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
def tucci(number):
    global count
    count += 1
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if number == 1:
        return 15
    elif number == 2:
        return 29
    else:
        return tucci(number-1) / tucci(number-2)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

count = 0

# You need to call the `tucci` function below
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

res = tucci(n)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
# %.5f implies that the variable after the percent sign `%` will have precision of exactly 5 decimal points
print('Result: %.5f' % res)
print('Count:', count)