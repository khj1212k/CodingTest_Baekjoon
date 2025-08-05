import re 

def solution(babbling):
    return sum(1 for b in babbling if re.compile('^(aya|ye|woo|ma)+$').match(b))