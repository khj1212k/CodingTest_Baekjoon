def solution(land):
    
    for i in range(len(land)-1): # 행 -> 행

        for j in range(4): # 열 -> 열
             # 첫줄i j열 가져와서, 다음줄i+1 j열뺀 다른 수 중에 제일 큰 수 [i+1,j]에 더하기
            land[i+1][j] += max([land[i][h] for h in range(4) if j != h])                

    return max(land[-1])
