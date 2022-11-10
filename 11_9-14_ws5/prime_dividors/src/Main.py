
file_name = input()
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

file = open(file_name)
n = int(file.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
def Prime_Factorial(n):
#You have to code a function that finds all prime divisors of this number n and prints it in ascending order. If a number n is dividing a prime number several times, you must print that prime number as much as it is divided.

#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if n < 4:
        return n
    for z in range (1, n):
        if n<=1:
            break
        for i in range(2, int(2+n//2)):
            if i == (1 + n // 2):
                print(n)
                n = n // n
            if n % i == 0:
                print(i)
                n = n // i
                break

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------

Prime_Factorial(n)

