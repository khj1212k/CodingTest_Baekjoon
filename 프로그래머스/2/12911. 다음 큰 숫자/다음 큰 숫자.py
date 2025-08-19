def solution(n):
    ones = str(bin(n)[2:]).count('1')
    for i in range(n+1,1000001):
        if ones == str(bin(i)[2:]).count('1'):
            return i
