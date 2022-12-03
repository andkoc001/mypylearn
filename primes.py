# Based on YouTube video at: https://youtu.be/03Uw0P08Mj4 

import numpy as np

def is_prime(num):
    if num == 2 or num == 3: return True
    if num < 2 or not num % 2: return False
    for i in range(3, int(num**.5 + 1), 2):
        if not num % i:
            return False
    return True

if __name__ == '__main__':
    # primes = [str(i) for i in range(100) if is_prime(i)]
    # print(', '.join(primes))
    
    
    # Ulam's Primes sprial
    size = 13
    max_num = size * size
    arr = np.zeros((size, size))
    pos = np.array([size, size]) // 2
    step = 1
    num = 1
        
    for iterations in range (0, size * size):
        for i in range(iterations):
            if num == max_num:
                break
            arr[pos[1], pos[0]] = num if is_prime(num) else 0
            pos[0] -= step
            num += 1
        for i in range(iterations):
            if num == max_num:
                break
            arr[pos[1], pos[0]] = num if is_prime(num) else 0
            pos[1] += step
            num += 1
        step *= -1
        
    print(arr)