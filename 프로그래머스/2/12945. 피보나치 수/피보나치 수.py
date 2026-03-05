def solution(n):
    # a:F(0), b:F(1)
    a, b = 0, 1
    aa = 0
    
    for _ in range(1, n):
        a, b = b ,a+b
        
    return b % 1234567