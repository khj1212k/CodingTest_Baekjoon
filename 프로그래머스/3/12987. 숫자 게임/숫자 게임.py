def solution(A, B):
    n = len(A)
    sort_A = sorted(A)
    sort_B = sorted(B)
    ai, bi = 0,0
    score = 0
    
    for _ in range(n):
        for __ in range(n):
            if ai==n or bi==n: return score
            if sort_A[ai] < sort_B[bi]: # 작은숫자들 부터 비교, B의 숫자가 더 크다면 
                score+=1
                ai+=1 # 다음꺼 비교
                bi+=1 # 다음꺼 비교
            else: # B가 더 작다면
                bi+=1
    
    
    return 