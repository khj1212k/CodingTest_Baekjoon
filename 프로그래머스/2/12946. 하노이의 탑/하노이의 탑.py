
        
def solution(n):
    
    def hanoi(n,start,end,sub):
        if n==1:
            yield [start,end]
        else:
            yield from hanoi(n-1,start,sub,end) # 맨밑에 제일큰거 빼고 n-1개를 sub기둥으로 옮김
            yield [start,end] # 맨밑에 있던 제일큰거를 end기둥으로 
            yield from hanoi(n-1,sub,end,start) # 나머지 sub에 있던걸 전부 end로 
        
    ans = list(hanoi(n,1,3,2))
    return ans