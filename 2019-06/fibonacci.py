# Andrzej Kocielski, 2019-06-27
# Calculates value of n-th number of the Fibonacci's sequence

###

print("Enter n-th number of Fibonacci's sequence: ")
n = int(input())


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


for n in range(1, n+1):
    print(n, ":", fib(n))
