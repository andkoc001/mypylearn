
def suma_cyfr(n):
    if n % 10 < 1:
        return 0
    else:
        return n%10 + suma_cyfr(n//10)
#suma_cyfr(123)


def pretty_print_numbers(num):
    if num < 10:
        print (num)
    else:
        pretty_print_numbers(num//10)
        print(num)
#pretty_print_numbers(4003)


def bunnyEars(b):
    if b == 0:
        return 0
    return (bunnyEars(b-1))+2
#bunnyEars(3)    




def suma(n):
    if n == 0:
        return 0
    return n+suma(n-1)
#print(suma(5))



def potega_1(p, n):
    if n == 0:
        return 1
    return 1/(p*(potega(p,(abs(n)-1))))
#print(potega(2,-3))

# dla n<0
def potega_2(p, n):
    q = 1/p
    m = abs(n)
    if m == 0:
        return 1
    else:
        return q*(potega(q,m-1))            
#print(potega(3,-4))
    
def potega(p, n):
    if n == 0:
        return 1
    elif n > 0:
        return p*potega(p,n-1)
    return (1/(p*potega(p,-n)))            
#print(potega(2,-3))

