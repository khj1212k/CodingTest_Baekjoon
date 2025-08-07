def solution(n, results):
    graph = [[] for i in range(n+1)]
    reverse_graph = [[] for i in range(n+1)]
    res = [[] for i in range(n+1)]
    
    [[graph[a].append(b),reverse_graph[b].append(a)] for a,b in results]
            
    for i in range(1,n+1):  
        wins, losses = 0, 0 
        
        q, visited = [i], [i]
        while q:            
            curr_node = q.pop(0)                
            for next_node in graph[curr_node]:  
                if next_node not in visited:    
                    visited.append(next_node)   
                    wins += 1                   
                    q.append(next_node)         
        
        q, visited = [i], [i]
        while q:            
            curr_node = q.pop(0)                
            for next_node in reverse_graph[curr_node]:  
                if next_node not in visited:    
                    visited.append(next_node)   
                    losses += 1                   
                    q.append(next_node) 
        
        res[i] = wins + losses
        
    return res.count(n-1)