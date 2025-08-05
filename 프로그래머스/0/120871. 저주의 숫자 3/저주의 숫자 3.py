# 3，6，9，12, 15...
# 13，23，33，...
def solution(n):
    cnt = 0
    answer = 0
    while cnt != n:
        answer += 1
        if (answer%3==0) or ('3' in str(answer)):
            continue    
        cnt += 1
    return answer