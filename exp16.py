'''
Power dgit sum
'''

if __name__ == "__main__":
    n = 2
    for i in range(1,1000):
        n = n*2
    lis = [int(d) for d in str(n)]
    sum = 0
    for l in lis:
        sum=sum+l
    print(sum)
