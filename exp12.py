'''
Highest Divisible Triangular Number
'''

def divisible_count(a):
    count = 0
    for i in range(1,a):
        if a % i == 0:
            count=count+1
    if count>=500:
        return True
    else:
        return False

def triangular():
    sum = 28
    i = 8
    while i<20000:
        sum=sum+i
        if divisible_count(sum) == False:
            i=i+1
        else:
            return i

if __name__ == "__main__":
    print(triangular())
