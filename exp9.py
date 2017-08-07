'''
Find pythogorean Triplet
'''

def checksum(a,b,c):
    if a+b+c==1000:
        return True
    else:
        return False

def pythogorean_triplet():
    for i in range(1,1000):
        for j in range(1,1000):
            for k in range(1,1000):
                if i*i+j*j==k*k:
                    if checksum(i,j,k):
                        return i*j*k


if __name__ == "__main__":
     print(pythogorean_triplet())
