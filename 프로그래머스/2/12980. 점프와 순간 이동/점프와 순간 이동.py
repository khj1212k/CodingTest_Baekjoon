def solution(n):
    ans = 0
    
    if n % 2 != 0 : # 홀수
        ans += 1
        n -=1
        
    while n not in [0,1]:
            print(n)
            n = n // 2
            if n % 2 != 0:
                ans += 1
                n -= 1


    return ans if n == 0 else ans+1