def solution(nodes, edges):
    answer = [0,0]
    parent = {x:x for x in nodes} # 루트 노드
    degree = {x:0 for x in nodes} # 노드의 차수
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
        
    def union(a,b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a == root_b:
            return False
        
        parent[root_b] = root_a
        return True
    
    for a,b in edges: 
        union(a,b) # 트리 구하기
        degree[a] += 1
        degree[b] += 1
    
    
    trees = {}
    for n in nodes: 
        root = find(n) # parent에 루트 노드만 남기기
        trees.setdefault(root, []).append(n)
    
    for r, tree in trees.items():
        OE = 0
        reverseOE = 0
        for node in tree:
            bool_n = node % 2 == 0
            bool_d = degree[node] % 2 == 0
            
            if bool_n == bool_d:
                OE += 1
            else: 
                reverseOE += 1
        
        if OE == 1 :
            answer[0] += 1
        if reverseOE == 1 :
            answer[1] += 1
            
    
    # print(f"{degree = }")
    # print(f"{trees = }")
    return answer