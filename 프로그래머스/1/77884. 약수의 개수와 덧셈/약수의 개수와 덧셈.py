def solution(left, right):
    answer = 0
    cnt = 0
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i%j == 0 : cnt += 1
        answer += i if cnt%2==0 else -i
        print(answer)
        cnt = 0
    return answer