def solution(k, score):
    li = []
    answer = []
    for i in score:
        li.append(i)
        li.sort()
        answer.append(min(li[-k:]))
    return answer