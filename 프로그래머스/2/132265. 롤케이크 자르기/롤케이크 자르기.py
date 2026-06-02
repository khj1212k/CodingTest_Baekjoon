from collections import Counter

def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)
    
    for t in topping:
        left.add(t)
        
        if right[t] == 1:
            right.pop(t)
        else:
            right[t] -= 1
        
        if len(right) == len(left):
            answer += 1
            
    return answer