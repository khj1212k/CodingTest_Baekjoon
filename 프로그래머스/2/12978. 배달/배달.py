import heapq
INF = 10**18

def solution(N, road, K):
    adj = [[] for _ in range(N+1)]
    for a,b,w in road:
        adj[a].append((b,w))
        adj[b].append((a,w))
    
    dist = [INF] * (N+1)
    dist[1] = 0
    pq = [(0,1)] # (거리, 노드)
    
    while pq:
        d, x = heapq.heappop(pq)
        if d > dist[x]: continue # 이미 더 짧은 거리로 방문 기록 있으면 넘김
        for nx, w in adj[x]:
            nd = d + w
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(pq, (nd,nx))

    return sum(1 for i in dist if i <= K)