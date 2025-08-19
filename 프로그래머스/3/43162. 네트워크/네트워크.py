def dfs(n, computers, visited, start):
    visited[start]=True
    for i in range(n):
        if computers[start][i] == 1 and not visited[i]:
            dfs(n, computers, visited, i)
    
def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    for i in range(n): # 모든 컴퓨터를 순회
        if not visited[i]: # 새로운 네트워크 발견!
            cnt+=1
            dfs(n,computers,visited,i)

    return cnt