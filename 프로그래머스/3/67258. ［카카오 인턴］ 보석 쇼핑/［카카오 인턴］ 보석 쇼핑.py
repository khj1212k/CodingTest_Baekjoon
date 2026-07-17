def solution(gems):
    total_types = len(set(gems))
    included_types = 0
    
    left = 0
    best_left = 0
    best_right = len(gems) - 1
    
    counts = {}
    
    for right, gem in enumerate(gems):
        # right move
        if counts.get(gem, 0) == 0:
            included_types += 1
            
        counts[gem] = counts.get(gem,0) + 1
        
        # left move
        while included_types == total_types: # all type in dict
            if right - left < best_right - best_left:
                best_right, best_left = right, left
            
            left_gem = gems[left]
            counts[left_gem] -= 1
            
            if counts[left_gem] == 0: included_types -= 1
            
            left += 1
    
    return [best_left+1, best_right+1]