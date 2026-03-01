def solution(s):
    cnt, zeros = 0, 0
    while s != '1':
        cnt+=1
        zeros += s.count('0')
        s = bin(s.count('1'))[2:]
    return [cnt, zeros]