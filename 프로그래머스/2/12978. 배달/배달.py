import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    INF = float('inf')
    dist = [INF]*(N+1)
    dist[1] = 0

    pq = [(0,1)] # cur_dist, node
    
    while pq:
        cur_dist, node = heapq.heappop(pq)
        
        if cur_dist > dist[node]: continue
        
        for next_node, cost in graph[node]:
            new_dist = cur_dist+cost
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    
    return sum(d<=K for d in dist)