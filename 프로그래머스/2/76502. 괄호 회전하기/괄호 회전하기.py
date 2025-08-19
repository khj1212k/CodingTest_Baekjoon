def is_correct_brackets(s):
    stack = []
    opn = '([{'
    cls = ')]}'
    
    for br in s:
        if br in opn:
            stack.append(br)
        else:
            if not stack:
                return False
            
            top = stack.pop()
            if cls.index(br) != opn.index(top):
                return False
    
    return not stack

def solution(s):
    n = len(s)
    answer = 0
    
    for i in range(n):
        rotated_s = s[i:] + s[:i]
        if is_correct_brackets(rotated_s):
            answer += 1
            
    return answer