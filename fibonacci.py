# Andrzej Kocielski, 2019-06-27
# Calculates value of n-th number of the Fibonacci's sequence with Memorisation funtionality
# Adopted from https://youtu.be/Qk0zUZW-U_M by Socratica

###

print("Enter n-th number of Fibonacci's sequence: ")
n = int(input())

# Memorisation funtionality stores in cache previously calculated values and return it without calculating again

fib_cache = {}  # Empty cache (dictionary data type)


def fib(n):
    # If the value has been cached, it will return it
    if n in fib_cache:
        return fib_cache[n]  # note data type

    # Compute n-th number value
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n-1) + fib(n-2)

    # Cache the value and return it
    fib_cache[n] = value
    return value


for n in range(1, n+1):
    print(n, ":", fib(n))
