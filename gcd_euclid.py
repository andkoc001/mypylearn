# Greatest common divisor 
# from lecture slides

def euclid(a, b):
    if b==0:
        return a
    else:
        return euclid(b, a%b)


def fib_2(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib_2(n-1) + fib_2(n-2)

#print(fib_2(6))


def potega(p, n):
  if n == 0:
    return 1
  elif (n-1) < 0:
    return p*(potega(p,(1/(n-1))))
  return p*(potega(p,n-1))

print(potega(3,.1))

