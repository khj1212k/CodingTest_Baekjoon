def solution(people, limit):
    left , right = 0, len(people)-1
    people.sort()
    cnt = 0
    
    while left <= right:
        cnt += 1
        if (people[right]+people[left]) <= limit: # 최소무게+최고무게 <= limit 
            left += 1
            right -= 1
        else: right -= 1 # 두사람합 무게초과면 최고무게가 타고나가
    
    return cnt