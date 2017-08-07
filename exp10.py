'''
Find sum of 2 million prime number
'''

def primes(n):
    primes = [2]
    attempt = 3
    sum = 0
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    yield sum(primes)

if __name__ == "__main__":
    print(next(primes(2000000)))
