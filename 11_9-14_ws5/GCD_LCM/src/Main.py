
file_name = input()

#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
file = open(file_name)
n = int(file.readline())
s = int(file.readline())


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
def gcd(n,s):
#In GCD function, you should find the greatest common divisor of two values and print it.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if n > s:
        small = s
    else:
        small = n
    for i in range(1, small + 1):
        if ((n % i == 0) and (s % i == 0)):
            gcd = i
    print(gcd)


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
def lcm(n,s):
#In LCM function, you should find the least common multiple of two values and print it.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    for i in range(max(n, s), 1 + (n * s)):
        if i % n == i % s == 0:
            lcm = i
            print(lcm)
            break

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

gcd(n,s)
lcm(n,s)

