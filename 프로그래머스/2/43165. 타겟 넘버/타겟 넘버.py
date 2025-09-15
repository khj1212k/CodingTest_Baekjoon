def solution(numbers, target):
    
    def dfs(idx, summ):
        if idx == len(numbers):
            return 1 if summ == target else 0
        return dfs(idx+1, summ + numbers[idx]) + dfs(idx+1, summ - numbers[idx])
    
    return dfs(0, 0)