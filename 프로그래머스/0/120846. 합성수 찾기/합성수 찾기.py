def solution(n):
    cnt = 0
    answer = 0
    for i in range(1,n+1): # 1~10
        cnt = 0
        for j in range(1,i+1): # 
            #약수 구하기
            if i % j == 0:
                cnt+=1
            # 약수 3개되면 합성수, answer+=1 하고 스탑    
            if cnt == 3:
                answer += 1
                break
    return answer