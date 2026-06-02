from itertools import product

def solution(word):

    return sorted(''.join(p) for n in range(1, 6) for p in product('AEIOU', repeat=n)).index(word) + 1