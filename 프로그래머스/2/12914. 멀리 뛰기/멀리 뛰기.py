

def solution(n):
    F = [1,2] + [0] * n
    
    for i in range(2, n+1):
        F[i] = (F[i-1] + F[i-2]) % 1234567
    
    return F[n-1]