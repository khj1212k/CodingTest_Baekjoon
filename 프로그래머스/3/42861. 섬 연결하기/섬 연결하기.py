def solution(n, costs):
    parents = list(range(n))
    total_cost = 0
    total_bridge = 0
    
    def find(child): # 부모를 찾는 함수
        if child != parents[child]: # 부모가 존재하면
            parents[child] = find(parents[child]) # 최종 부모를 찾아서 재귀
        return parents[child]
        
        return child
    
    def union(a,b): # 사이클인가?
        root_a = find(a)
        root_b = find(b)
        
        if root_a == root_b: # 같은 부모, 즉 ab가 연결되면 사이클
            return False
        
        parents[root_b] = root_a
        return True
    
    for a,b,cost in sorted(costs, key=lambda x: x[2] ):
        if union(a,b):
            total_cost += cost
            total_bridge += 1
            
        if total_bridge == n-1:
            break
        
    return total_cost