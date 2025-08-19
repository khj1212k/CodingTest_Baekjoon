#      1
#   1     2
#  1 2   3 4
# 12 34 56 78
# (4+1)//2 = 2  (2+1)//2 = 1
# (7+1)//2 = 4  (3+1)//2)= 2


def solution(n,a,b):
    cnt = 0
    
    while a != b:
        a = (a+1)//2
        b = (b+1)//2
        cnt += 1

    return cnt