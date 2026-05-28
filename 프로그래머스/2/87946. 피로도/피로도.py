from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons):
        cnt = 0
        fatigue = k
        
        for required, cost in p:
            if fatigue >= required:
                fatigue -= cost
                cnt += 1
                
        answer = max(answer, cnt)
    return answer