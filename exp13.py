'''
Sum of 100 numbers which are 50 digits long
'''

if __name__ == "__main__":
    sum=0;
    F = open('expthirteen.txt','r')
    for line in F:
        sum = sum + int(line)
    print(sum)
