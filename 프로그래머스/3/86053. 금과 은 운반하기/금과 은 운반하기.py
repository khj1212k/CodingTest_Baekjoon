# 시간 이진탐색, 그 시간안에 필요한 양의 광물들을 다 옮길수있는가

def solution(a, b, g, s, w, t):
    
    # T시간 안에 필요한 양의 광물들을 다 옮길 수 있는가
    def can(T, ncity):
        gold = silver = total = 0

        for i in range(ncity):
            cnt = T // (2*t[i]) # 왕복횟수
            if T % (2*t[i]) >= t[i]:  cnt+=1 # 편도 한번더 가능?

            move = cnt * w[i] # 트럭의 최대 운반가능 무게

            # min(가지고있는광물의무게 ,최대운반가능무게)
            gold += min(g[i], move)
            silver += min(s[i], move)
            total += min(g[i]+s[i], move) # 금은 동시에 운반시

        # 금, 은 , 총합 전부 T시간내에 운송 가능한가
        return gold>=a and silver>=b and total>=a+b

    left = 0
    right = 10**15
    ncity = len(t)
    
    # 시간 T 이진 탐색
    while left <= right:
        mid = (left + right) // 2
        
        if can(mid, ncity): # 운반가능
            answer = mid
            right = mid-1
        else: # 운반불가
            left = mid+1
        
    return answer