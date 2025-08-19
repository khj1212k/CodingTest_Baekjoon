# [7,9,1,1,4,7,9,1,1,4]

def solution(elements):
    li = elements+elements
    answer = []
    
    for lenn in range(len(elements)): # lenn 조합길이 1~5
        for i in range(len(elements)): # 순환 idx
            answer.append(sum(li[i:i+lenn+1]))

    return len(set(answer))