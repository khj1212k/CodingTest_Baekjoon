# def solution(participant, completion):
#     res = ''

#     participant.sort()
#     completion.sort()

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             res = participant[i]
#             break

#     if not res:
#         res = participant[-1]

#     return res
def solution(participant, completion):

    temp = 0
    p = dict()
    c = dict()

    for i in participant:
        p[hash(i)] = i
        temp += hash(i)

    for i in completion:
        # c[hash(i)] = i
        temp -= hash(i)

    
    return p[temp]