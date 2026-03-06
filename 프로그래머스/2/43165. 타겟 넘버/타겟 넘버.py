def solution(numbers, target):
    answer = 0
    sums = 0
    
    def dfs(idx, sums):
        nonlocal answer
        if len(numbers) == idx:
            if sums == target: 
                answer += 1
            return
            
        dfs(idx+1, sums+numbers[idx])
        dfs(idx+1, sums-numbers[idx])
        
    dfs(0,sums)
    return answer