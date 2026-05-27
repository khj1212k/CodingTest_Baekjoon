from collections import defaultdict

def solution(sales, links):
    n = len(sales)
    
    teams = [[] for _ in range(len(sales)+1)]
    for a,b in links:  teams[a].append(b)
    
    # [참석시 최소비용, 미참석시 최소비용]
    dp = [[0,0] for _ in range(len(sales)+1)]
    
    def dfs(x):
        dp[x][1] = sales[x-1] # 참석시 본인 비용 
        
        if not teams[x]: return # 말단직원
        
        attend_child = False
        extra_cost = float('inf')
        
        for child in teams[x]: # 직속 부하들 먼저 계산
            dfs(child)
            
            dp[x][1] += min(dp[child][0], dp[child][1]) # x참석시
            
            # x불참시, 직속 중 1명 참석해야함
            dp[x][0] += min(dp[child][0], dp[child][1]) 
            
            # 자식 참석이 더 싸면, x불참
            if dp[child][1] <= dp[child][0]:
                attend_child = True
            
            # 자식을 강제참석시, 추가비용이 가장 적은 자식 찾기
            extra_cost = min(extra_cost, dp[child][1] - dp[child][0])
        
        # x불참 자식들 불참시, 가장 적은 추가비용으로 자식 한명 참석
        if not attend_child:
            dp[x][0] += extra_cost
            
    dfs(1) # ceo부터 시작
        
    return min(dp[1][0], dp[1][1])