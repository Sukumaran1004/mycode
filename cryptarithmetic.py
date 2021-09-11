import itertools
from itertools import *
import string

def solve_crypt_arithmetic(problem):
    problem= problem.lower() # convert given words to lowercase
    leftside,rightside=problem.replace('','').split('=') # split the word to lefthandside and righthandside by =
    leftside=leftside.split('+') # then split the lefthandside to two
    letters=set(rightside)  #create a set of used letters
    for words in leftside:
        for letter in words:
            letters.add(letter)   # add function is used to remove duplicates of element
    letters=list(letters)    # set elements are converted into list
    number=range(10) # to give list of 0-9 numbers
    for permutation in itertools.permutations(number,len(letters)):  # itertools permutation are used to give combination of letters
        solution=dict(zip(letters,permutation))    # zip function is used to accept iterable items and merge to single tuple

        if sum(get_factor(words,solution) for words in leftside)==get_factor(rightside,solution):
            print('+'.join(str(get_factor(words,solution) )for words in leftside)+"={}(mapping:{})".format(get_factor(rightside,solution),solution))



def get_factor(words,sub):
    s=0
    factor=1
    for letter in reversed(words):
        s+=factor*sub[letter]
        factor=factor*10

    return s

if __name__=='__main__':
    solve_crypt_arithmetic('send+more=money')



