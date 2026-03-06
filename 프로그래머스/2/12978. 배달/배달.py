import heapq


def solution(N, road, K):
    INF = float('inf')
    
    graph = [[] for _ in range(N+1)]
    for a,b,w in road:
        graph[a].append((b,w))
        graph[b].append((a,w))
    
    dist = [INF] * (N+1)
    dist[1] = 0
    pq = [(0,1)] # (거리, 노드)
    
    while pq:
        cur_dist, node = heapq.heappop(pq)
        if cur_dist > dist[node]: continue # 이미 더 짧은 거리로 방문 기록 있으면 넘김
        for next_node, cost in graph[node]:
            new_dist = cur_dist + cost
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist,next_node))

    return sum(d <= K for d in dist)