from collections import defaultdict

def solution(topping):
    answer = 0
    left = set() # 기준선 왼쪽에 있는 토핑의 종류
    right = defaultdict(int)
    
    for i in topping:
        right[i] += 1
    
    for t in topping:
        left.add(t)
        
        if right[t] == 1:  del right[t] 
        else:              right[t] -= 1
        
        if len(left) == len(right): 
            answer += 1
        
    return answer