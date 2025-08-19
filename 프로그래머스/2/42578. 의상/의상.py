from collections import defaultdict

def solution(clothes):
    dd = defaultdict(int)
    answer = 1
    
    for v,k in clothes:
        dd[k]+=1
    
    for n in dd.values(): 
        answer *= (n+1)
    
    return answer-1