from collections import Counter

def solution(s):
    zeros_cnt = 0
    s = [i for i in s]
    cnt = 0
    while s != ['1']:
        ones = Counter(s)['1']
        zeros_cnt += Counter(s)['0']
        s = [i for i in format(ones,'b')]
        cnt += 1
        
        print( f'{cnt= } ', f'{zeros_cnt= } ', f'{s= }')
    return [cnt, zeros_cnt]