# 이것도 그리디 문제 같은데?

def solution(n, stations, w):
    answer = 0
    start = 1
    cover = 2*w+1
    
    for station in stations+[n+w+1]:
        left = station-w
        if start < left : 
            gap = left - start
            answer += (gap-1) // cover + 1
        start = max(start,station+w+1)
    
    return answer