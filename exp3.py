
'''
Largest Prime Factor
'''

import math

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return max(primfac)

if __name__ == "__main__":
    print(primes(600851475143))
