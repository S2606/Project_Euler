'''
Difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
'''

def each_square(n):
    "Generate squares of each number"
    seen = list()
    sum = 0
    for i in range(1, n+1):
        seen.append(i)
    squares=map(lambda n: n*n, seen)
    for j in squares:
        sum=sum+j
    return sum

def total_square(n):
    "Generate square of sum of all number"
    sum=0
    for i in range(1, n+1):
        sum=sum+i
    return sum*sum

if __name__ == "__main__":
    print(total_square(100)-each_square(100))
