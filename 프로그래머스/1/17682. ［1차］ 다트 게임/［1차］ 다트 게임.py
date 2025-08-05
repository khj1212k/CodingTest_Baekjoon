import re

def solution(dartResult):
    li = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    answer = [0]*4
    for idx, i in enumerate(li):
        n,v,s = i
        answer[idx] = (int(n) ** ' SDT'.index(v))
        answer[idx] *= -1 if s=='#' else 1
        if s == '*': 
            for j in range(idx-1,idx+1):
                answer[j]*=2
    return sum(answer)