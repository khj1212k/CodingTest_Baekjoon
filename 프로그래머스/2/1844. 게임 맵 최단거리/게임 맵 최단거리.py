from collections import deque

def solution(maps):
        h, w = len(maps), len(maps[0])
        dist = [[-1]*w for _ in range(h)]
        dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # 상하좌우
        q = deque([(0,0)])
        dist[0][0] = 1

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if not(0<=nx<w and 0<=ny<h) : continue
                if maps[ny][nx] == 0 or dist[ny][nx] != -1: continue
                q.append([nx,ny])
                dist[ny][nx] = dist[y][x] + 1

        return dist[h-1][w-1]

        