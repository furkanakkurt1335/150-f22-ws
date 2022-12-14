# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

filename = input()
fh = open(filename, 'r')
l = fh.read().split('\n')

early, late = 0, 0
for i in l:
    early, late = late, int(i)
    sum_t = early+late
    if sum_t % 3 == 0:
        print(sum_t)
    elif sum_t % 3 == 1:
        print(sum_t**2)
    elif sum_t % 3 == 2:
        print(sum_t % 10)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
