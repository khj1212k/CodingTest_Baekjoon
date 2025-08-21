# 7
#   10    8
# 18 11(9) 18
# 

#   0
#  0 1
# 0 1 2
# 

def solution(triangle):
    answer = 0
    ans = [[0]*(i+1) for i in range(len(triangle))]
    ans[0][0] = triangle[0][0]
    
    try:
        for i in range(len(triangle)-1): # 전체리스트 위에서 아래로 idx
            
            for j in range(len(ans[i])): # 윗리스트 순환 val, 아랫값 2개에 추가해서 ans에 넣을거  
                    if triangle[i+1][j]+ans[i][j] > ans[i+1][j]:# 기존 ans(오른쪽)
                        ans[i+1][j] = triangle[i+1][j]+ans[i][j] # ans(오른쪽) = 밑(오른쪽) + 위 
                    ans[i+1][j+1] = triangle[i+1][j+1]+ans[i][j] # ans(왼쪽) = 및(왼쪽) + 위 
                    pass
        return max(ans[-1])
    
    except Exception as e:
        print(ans)
        print(f"에러가 발생했습니다: {e}")
