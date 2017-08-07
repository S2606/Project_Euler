'''
Find 10001st prime number
'''

def primes(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]

if __name__ == "__main__":
    print(primes(10001))
