'''
Find Longest Collatz sequence
'''

Dict = {}

def Series(N):
    Counter = 1
    Original = N
    while N != 1:
        N = N/2 if N % 2 == 0 else 3*N+1
        if N in Dict:
            Counter += Dict[N]
            Dict [Original] = Counter
            return Counter
        Counter += 1
    Dict [Original] = Counter
    return Counter


Max, Element = 0, 0
for x in range (1, 1000000):
    series = Series(x)
    if (Max < series):
        Max = series
        Element = x

print(Max, Element)
