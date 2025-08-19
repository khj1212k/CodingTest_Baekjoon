def solution(n):
    if n == 0: return 0
    F = [0] * (n+1)
    
    F[0],F[1] = 0,1
    
    for i in range(2,n+1):
        F[i] = (F[i-1] + F[i-2]) % 1234567

    return F[n]