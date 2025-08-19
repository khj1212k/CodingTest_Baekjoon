# 1234
# 2234
# 3334
# 4444

def solution(n, left, right):
    li = []
    for row in range(1,n+1):
        for col in range(1,n+1):
            li.append(col if row < col else row)
    return li[left:right+1]

def solution(n, left, right):
    return [max((i//n,i%n))+1 for i in range(left,right+1)]