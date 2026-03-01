def solution(n):
    cnt = 1
    for i in range(1, n//2+1):
        sums = 0
        # print()
        for j in range(i,n):
            # print(f'{i=} ', f'{j=}')
            sums += j
            if sums == n:
                cnt+=1
                # print(cnt)
                break
            elif sums > n:
                break
        
    return cnt