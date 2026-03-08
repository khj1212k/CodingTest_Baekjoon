import heapq # 최소힙

def solution(n, works):
    if sum(works)<=n: return 0
    
    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        w = heapq.heappop(works) # 최소값 뱉음
        heapq.heappush(works, w+1)
        # print(works)
        
    return sum((-w)**2 for w in works)