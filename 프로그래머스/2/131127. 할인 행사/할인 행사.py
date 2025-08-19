from collections import Counter

def solution(want, number, discount):
    n = sum(number)
    want_c = Counter({k:v for k,v in zip(want,number)})
    cnt = 0
    
    for i in range(len(discount)-n+1):
        if not (want_c - Counter(discount[i:i+n])):
            cnt+=1

    return cnt