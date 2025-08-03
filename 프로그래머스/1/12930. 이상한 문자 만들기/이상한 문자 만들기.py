def solution(s):
    answer = ''
    li = s.split(' ')
    for l in li:
        for i in range(len(l)):
            if i%2!=0 : answer = answer + l[i].lower()
            else : answer=answer + l[i].upper()
        answer += ' '
    return answer[:-1]