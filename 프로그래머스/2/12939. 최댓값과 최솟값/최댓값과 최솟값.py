def solution(s):
    s = [*map(int, s.split())]
    return str(min(s))+' '+ str(max(s))