# Read the file
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
f = open(filename, 'r')
n = int(f.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
def bucci(number):
    global count
    count += 1
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if number == 1:
        return 4
    elif number == 2:
        return 7
    else:
        return bucci(number-1) + bucci(number-2)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

count = 0

# You need to call the `bucci` function below
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

res = bucci(n)
print('Result:', res)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

print('Count:', count)