import re

def solution(my_string):
    return [int(i) for i in sorted(re.findall('\d', my_string))]