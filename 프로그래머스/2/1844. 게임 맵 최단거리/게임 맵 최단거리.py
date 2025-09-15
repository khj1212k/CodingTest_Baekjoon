from collections import deque

def solution(maps):
    # 상하좌우
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    rows, cols = len(maps), len(maps[0])
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not (0 <= nx < rows and 0 <= ny < cols): continue # 맵 벗어남
                if maps[nx][ny] == 0 : continue # 벽 무시
                if maps[nx][ny] == 1: # 처음 지나가는 거리
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))
                    
        res = maps[rows - 1][cols - 1]
        return -1 if res == 1 else res
    
    return bfs(0,0)