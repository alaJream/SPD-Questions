# Create a function that returns the factorial of any positive input number
# Helpful tip: Try to solve the problem comfortably in code before trying it recursively
# Problem
# Factorial is:

# 4! ==> 4 x 3 x 2 x 1

# we want to have user input the number
# go through the factorial function
# print out factorial_number


def factorial_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_number(n-1)

n = int(input("Enter a number to calculate its factorial: "))
result = factorial_number(n)
print("The factorial of", n, "is", result)

# n takes in the factorial of (n * n-1)
# it'll return n=1 if n is =0 or =1 then it's done
# Otherwise the function calls itself with n-1 and multiplies by the result of n
# This calculates the factorial

