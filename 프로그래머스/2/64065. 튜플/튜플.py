import re
from collections import Counter

def solution(s):
    return list(map(int, [k for k,v in sorted(Counter(re.findall(r'\d+', s)).items(), key=lambda x : x[1], reverse=True)]))