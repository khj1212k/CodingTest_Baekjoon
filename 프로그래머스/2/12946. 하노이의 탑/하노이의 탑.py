
        
def solution(n):
    answer = []
    
    def hanoi(n,start,end,sub):
        if n==1:
            answer.append([start,end])
        else:
            hanoi(n-1,start,sub,end) # 맨밑에 제일큰거 빼고 n-1개를 sub기둥으로 옮김
            answer.append([start, end]) # 맨밑에 있던 제일큰거를 end기둥으로 
            hanoi(n-1,sub,end,start) # 나머지 sub에 있던걸 전부 end로 
        
    hanoi(n,1,3,2)
    return answer