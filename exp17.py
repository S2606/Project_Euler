'''
Number Letter Word
'''
import inflect

if __name__ == "__main__":
    p = inflect.engine()
    sum = 19
    for i in range(6,1001):
        word = p.number_to_words(i)
        sum = sum + len(word) - word.count(' ') - word.count('-')
    print(sum)
