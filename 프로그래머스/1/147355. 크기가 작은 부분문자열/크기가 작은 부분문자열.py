# def solution(t, p):
#     answer = 0
#     for i in range(len(t)-len(p)+1):
#         print(i, t[i:+i+len(p)])
#         if p >= t[i:+i+len(p)]:
#             # print(p, t[i:+i+len(p)])
#             answer += 1
#     return answer

def solution(t, p):
    return sum(1 for i in range(len(t)-len(p)+1) if p >= t[i:+i+len(p)])
