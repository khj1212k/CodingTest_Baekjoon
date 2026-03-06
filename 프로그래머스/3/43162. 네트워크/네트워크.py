from collections import deque

def bfs(start, adj, visited):
    q = deque([start])
    visited[start] = True
    
    while q:
        x = q.popleft()
        nx_li = adj[x]
        for nxi in range(len(nx_li)):
            if visited[nxi] or nx_li[nxi] == 0:
                continue
            q.append(nxi)
            visited[nxi] = True
        

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1
    return answer