# Read the file
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
f = open(filename, 'r')
n = int(f.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
def fibomulti(number):
    global count
    count += 1
#The function youre going to complete should return the product of the two previous result using recursion.
#It's like fibonacci, but we use multiplication instead of addition. first value 2, second value 3. Ignore the count val
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if number == 1:
        return 2
    elif number == 2:
        return 3
    else:
        return fibomulti(number-1) * fibomulti(number-2)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

count = 0

# You need to call the `fibomulti` function below
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

res = fibomulti(n)
print('Result:', res)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

print('Count:', count)