from itertools import combinations

def solution(number):
    return sum(1 for c in combinations(number, 3) if sum(c) == 0)