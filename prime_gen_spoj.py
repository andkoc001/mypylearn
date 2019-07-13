# Andrzej Kocielski, 2019-07-10
# SPOJ.com solution to problem Prime generator, https://www.spoj.com/problems/PRIME1/.
###

# Import of required modules
import math  # this module includes square root method
import time  # for duration of calculation

m = 10
n = 22

# Number of test cases - entered by user, t<=10
t = int(input("Number of test cases (max 10 tests): "))
if t <= 10:

    # For each test case the user enters lower (m) and upper (n) limit for the test, 1<=m<=n<=1000000000, n-m<=100000
    for i in range(t):

        m = int(input("Lower limit: "))
        n = int(input("Upper limit: "))
        if 1 <= m <= n <= 1000000000 and n-m <= 100000:

            # Calculation time
            # t0 = time.time()

            if m < 2:
                m = 2
                for num in range(m, n+1):
                    # Credits to Socratica https://youtu.be/2p3kwF04xcA
                    for j in range(2, 1+math.floor(math.sqrt(num))):
                        if num % j == 0:
                            break
                    else:
                        print(num)
                        pass

                # t1 = time.time()
                # print(t1-t0)
        else:
            print("1 <= lower <= upper <= 1000000000 and upper-lower <= 100000")
else:
    print("Too many tests.")
