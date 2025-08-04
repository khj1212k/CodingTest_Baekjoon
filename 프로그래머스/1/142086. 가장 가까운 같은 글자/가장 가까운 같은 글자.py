def solution(s):
    answer_li = [-1]
    for i in range(1,len(s)):
        if s[i] in s[:i] : answer_li.append(i - s[:i].rindex(s[i]))
        else : answer_li.append(-1)
            
    return answer_li