import math

def solution(arr):
    a = arr.pop()
    
    for b in arr:
        a = abs(a * b) // math.gcd(a, b)
    return a