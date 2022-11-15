# Read the file
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
f = open(filename, 'r')
s1 = int(f.readline())
s2 = int(f.readline())
n = int(f.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
def phobicnacci(number):
    global count
    count += 1
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if number == 1:
        return s1
    elif number == 2:
        return s2
    else:
        first = phobicnacci(number-1)
        second = phobicnacci(number-2)
        if(first % 2 == 0 and second % 2 == 0):
            return int((first/2)) + (2*second+1)
        else:
            return first + second


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

count = 0

# You need to call the `phobicnacci` function below
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

res = phobicnacci(n)
print('Result:', res)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

print('Count:', count)