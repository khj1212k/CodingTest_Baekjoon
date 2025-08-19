def is_correct(s):
    opn, cls = '([{', ')]}'
    stack = []
    
    for br in s:
        if br in opn: # 여는 괄호
            stack.append(br)
        else: # 닫는 괄호 
            if not stack: # 닫는괄호가 들어왔는데 스택이 비어있는 경우
                return False
            top = stack.pop() # 스택이 안 빈 경우
            if cls.index(br) != opn.index(top): # 괄호의 종류가 다를경우
                return False
    return not stack # 순환이 끝나고 스택이 비었으면 정상True, 아직 남았으면 False
    
def solution(s):
    return sum(1 for i in range(len(s)) if is_correct((s*2)[i:i+len(s)]))