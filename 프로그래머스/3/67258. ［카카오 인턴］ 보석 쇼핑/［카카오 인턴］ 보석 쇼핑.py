def solution(gems):
    total_types = len(set(gems))
    counts = {}
    
    left = 0
    best_start = 0
    best_end = len(gems) - 1
    included_types = 0

    for right, gem in enumerate(gems):
        if counts.get(gem, 0) == 0:
            included_types += 1
        
        counts[gem] = counts.get(gem, 0) + 1

        while included_types == total_types:
            if right - left < best_end - best_start:
                best_start = left
                best_end = right

            left_gem = gems[left]
            counts[left_gem] -= 1

            if counts[left_gem] == 0:
                included_types -= 1

            left += 1

    return [best_start + 1, best_end + 1]