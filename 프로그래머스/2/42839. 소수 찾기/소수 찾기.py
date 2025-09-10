from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    li = set()
    answer = 0
    
    for i in range(len(numbers)):
        for p in permutations(numbers,i+1):
            num = int(''.join(p))
            if is_prime(num):
                li.add(num)
    
    return len(li)