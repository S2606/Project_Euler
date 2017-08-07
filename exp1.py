
'''
Sum of number which are multiples of 3 or 5 
'''

import math

if __name__ == "__main__":
    count=0
    for i in range(1,1000):
        if(i%3==0 or i%5==0):
            count=count+i
    print(count)
