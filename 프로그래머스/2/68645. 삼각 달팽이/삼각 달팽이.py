def tri(n):
    if n < 4: # n=3 이하, 내부삼각형 없음
        if   n == 1: return [[1]]
        elif n == 2: return [[1], [2,3]]
        elif n == 3: return [[1], [2,6], [3,4,5]]
            
    else: # n=4 이상, 내부 삼각형 있음
        inner = [[i+(n-1)*3 for i in li] for li in tri(n-3)]
        outer = [[],[]] + inner + [[]]
        down, up = 0, n-1

        [outer[i].insert(0,i+1) for i in range(0,n-1)]
        [outer[-1].append(i+1) for i in range(n-1,2*(n-1))]
        [outer[3*(n-1)-i].append(i+1) for i in range(2*(n-1),3*(n-1))]
            
    return outer
    
def solution(n):
    return [i for li in tri(n) for i in li ] 