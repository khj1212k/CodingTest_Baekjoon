def solution(n, results):
    graph = [[] for i in range(n+1)]
    reverse_graph = [[] for i in range(n+1)]
    res = [[] for i in range(n+1)]
    
    for a,b in results:
        graph[a].append(b)
        reverse_graph[b].append(a)
        
    # print('graph',graph)
    # print('reverse_graph',reverse_graph)
    
    for i in range(1,n+1):  # 시작점 1,2,3,4,5
        q = [i]             # 큐에 1 넣고 시작
        visited = [i]       # 방문 1 넣고 시작
        wins, losses = 0, 0 # 1이 이긴수, 진수
        
        while q:            # q가 빌때까지
            # print('q',q)
            curr_node = q.pop(0)                # q 맨앞수 1 가져와
            for next_node in graph[curr_node]:  # 1 이랑 이어진 노드들 차례로 2
                if next_node not in visited:    # 2가 방문에 없다면
                    visited.append(next_node)   # 방문에 [1,2]
                    wins += 1                   # 승+1
                    q.append(next_node)         # 다음노드 2를 q에 추가
        # print(i, 'wins', wins)
        
        q = [i]
        visited = [i]
        
        while q:            # q가 빌때까지
            # print('q',q)
            curr_node = q.pop(0)                
            for next_node in reverse_graph[curr_node]:  # 이번엔 역그래프로 패배 수 계산
                if next_node not in visited:    
                    visited.append(next_node)   
                    losses += 1                   
                    q.append(next_node) 
        # print(i, 'losses', losses)
        
        res[i] = wins + losses
        # print('res',res)
        
    answer = res.count(n-1)
    return answer