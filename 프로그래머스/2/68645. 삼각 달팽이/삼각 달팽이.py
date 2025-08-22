# n=4 (~9 = 3*3)  -> n=1 (10)
# n=5 (~12 = 4*3) -> n=2 (13 / 14,15)
# n=6 (~15 = 5*3) -> n=3 (16 / 17,21 / 18,19,20)
# n=7 (~18 = 6*3) -> n=4 (19 ~ 27  = 3*3)-> n=1 (28)

# n=3 
# li[0][0] = 1

# [1,
# 2,18,
# 3,19,17,
# 4,20,27,16,
# 5,21,28,26,15,
# 6,22,23,24,25,14,
# 7,8,9,10,11,12,13]

def tri(start):
    try:
        
        if start < 4: # n=3 이하, 내부삼각형 없음
            if  start == 1:
                return [[1]]
            elif start == 2:
                return [[1], [2,3]]
            elif start == 3:
                return [[1], [2,6], [3,4,5]]
            
        else: # n=4 이상, 내부 삼각형 있음
            inner = [[i+(start-1)*3 for i in li] for li in tri(start-3)]
            outer = [[],[]] + inner + [[]]
            down, up = 0, start-1

            [outer[i].insert(0,i+1) for i in range(0,start-1)]
            [outer[-1].append(i+1) for i in range(start-1,2*(start-1))]
            [outer[3*(start-1)-i].append(i+1) for i in range(2*(start-1),3*(start-1))]
            
            return outer
        
    except Exception as e:
            print(e)
    
def solution(n):
    return [i for li in tri(n) for i in li ] 