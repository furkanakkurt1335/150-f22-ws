
file_name = input()

#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
file = open(file_name)
n = int(file.readline())
s = int(file.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
def gcd(n, s):
#In the function `GCD`, you should find the greatest common divisor of the two values and print it.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if n > s:
        small = s
    else:
        small = n
    gcd_t = 0
    for i in range(1, small + 1):
        if ((n % i == 0) and (s % i == 0)):
            gcd_t = i
    print(gcd_t)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
def lcm(n, s):
#In the function `LCM`, you should find the least common multiple of the two values and print it.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    lcm_t = -1
    for i in range(max(n, s), 1 + (n * s)):
        if i % n == i % s == 0:
            lcm_t = i
            print(lcm_t)
            break

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

gcd(n, s)
lcm(n, s)

