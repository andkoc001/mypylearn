# Andrzej Kocielski, 2019-07-10
# SPOJ.com solution to problem Prime generator, https://www.spoj.com/problems/PRIME1/.
###

# Import of required modules
import math  # this module includes square root method

# Number of test cases - entered by user, t<=10
# t = int(input("Number of test cases: "))

# For each test case the user enters lower (m) and upper (n) limit for the test, 1<=m<=n<=1000000000, n-m<=100000
# for i in range(t):
# m = int(input("Lower limit: "))
# n = int(input("Upper limit: "))

for j in range(2, 12+1):
    if 12 % j != 0:
        print(j)
