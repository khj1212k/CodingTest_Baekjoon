def solution(n):
    if n==1:return 0
    cnt = 0
    while cnt != 500:
        n = n/2 if n%2==0 else (n*3)+1
        cnt += 1
        if n == 1 : return cnt
    return -1