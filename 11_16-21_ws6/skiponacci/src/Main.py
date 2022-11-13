# Read the file
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
f = open(filename, 'r')
n = int(f.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
def skiponacci(number):
    global count
    count += 1
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if number == 1:
        return 3
    elif number == 2:
        return 0
    elif number == 3:
        return 2
    else:
        return skiponacci(number-2) + skiponacci(number-3)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

count = 0

# You need to call the `skiponacci` function below
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

res = skiponacci(n)
print('Result:', res)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

print('Count:', count)
