# 남은일수 : ((100-progress) / speed)의 올림
#          ((100-30) / 30) = 2

# [5, 10, 1, 1, 20, 1]
# 5:1, 10:3, 20:1
# for l in left 에서 하나씩 제일큰수를 찾는다. max = l
# 다음 더 큰수가 올때까지 cnt+=1
# 그리고 그 다음 수가 더 큰수면 if l > max: answer.append(cnt), cnt = 1, max = l

from math import ceil

def solution(progresses, speeds):
    answer, stack = [], []
    left = [ceil((100-p)/s) for p, s in zip(progresses,speeds)]
    cnt, maxx = 1, 0
    
    for l in left:
        if l > maxx:
            answer.append(cnt)
            cnt = 1
            maxx = l
        else : 
            cnt += 1
    answer.append(cnt)
            
    return answer[1:]