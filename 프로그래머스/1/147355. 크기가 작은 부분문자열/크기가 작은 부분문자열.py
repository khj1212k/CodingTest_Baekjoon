def solution(t, p):
    l = len(p)
    cnt=0
    for i in range(len(t)-l+1):
        if int(t[i:i+len(p)]) <= int(p) : cnt+=1
        print(int(t[i:i+len(p)]) , int(p))
    return cnt