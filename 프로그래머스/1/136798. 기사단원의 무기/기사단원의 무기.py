def solution(number, limit, power):
    divisors_count = [0] * (number + 1)
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors_count[j] += 1
            
    total_weight = 0
    for i in range(1, number + 1):
        if divisors_count[i] > limit:
            total_weight += power
        else:
            total_weight += divisors_count[i]
            
    return total_weight