import heapq

def solution(n, edge):
    INF = int(1e9)
    start = 1
    # visited = [False] * n
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append((b,1))
        graph[b].append((a,1))
    # print(graph)
    
    def dijkstra(start):
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for next_node, weight in graph[now]:
                cost = dist + weight
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
    
    dijkstra(start)

    return distance[1:].count(max(distance[1:]))