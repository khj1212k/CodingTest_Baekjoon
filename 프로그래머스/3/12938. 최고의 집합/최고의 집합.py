# s를 n등분한 값들이 최대곱이 됨.

def solution(n, s):
    if s<n: return [-1]
    q, r = divmod(s, n)
    
    return [q] * (n-r) + [q+1] * r