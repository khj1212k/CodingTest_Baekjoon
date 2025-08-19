from collections import Counter

# def solution(want, number, discount):
#     n = sum(number)
#     want_c = Counter({k:v for k,v in zip(want,number)})
#     cnt = 0
    
#     for i in range(len(discount)-n+1):
#         if want_c == Counter(discount[i:i+n]):
#             cnt+=1

#     return cnt

def solution(want, number, discount):
    return sum(1 for i in range(len(discount)-sum(number)+1) if Counter({k:v for k,v in zip(want,number)}) == Counter(discount[i:i+sum(number)]))