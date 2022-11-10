
file_name = input()
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

file = open(file_name)
n = int(file.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
def prime_factorial(n):
# You have to code a function that finds all prime divisors of the number n and prints them in ascending order. If a prime number divides `n` several times, you must print that prime number as much as it divides `n`.

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

prime_factorial(n)

