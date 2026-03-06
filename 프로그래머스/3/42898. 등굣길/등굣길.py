def solution(m, n, puddles):
    answer = 0
    maps = [[0]*m for i in range(n)]
    maps[0][0] = 1
    for h in range(n):
        for w in range(m):
            if [w+1,h+1] in puddles or [h,w] == [0,0]: continue
            left = maps[h][w-1] if w!=0 else 0
            up = maps[h-1][w] if h!=0 else 0
            maps[h][w] = left + up
        
    return maps[n-1][m-1] % 1000000007