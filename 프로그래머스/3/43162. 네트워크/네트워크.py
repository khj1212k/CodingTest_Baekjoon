from collections import deque

def bfs(start, computers, visited):
    q = deque([start])
    visited[start] = True
    while q:
        x = q.popleft()
        nx_li = computers[x]
        for nxi in range(len(nx_li)):
            if visited[nxi] or nx_li[nxi] == 0:
                continue
            visited[nxi] = True
            q.append(nxi)


def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            cnt += 1
    return cnt