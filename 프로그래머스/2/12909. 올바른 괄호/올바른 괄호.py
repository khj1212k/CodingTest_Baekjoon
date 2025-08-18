def solution(s):
    stack = []
    
    for i in s:
        if i == '(': # 여는 괄호
            stack.append(i)
        elif i == ')': # 닫는 괄호
            if not stack: # 닫는괄호가 왔는데 여는괄호가 하나도 없다면 그건 이미 올바른 괄호가 아니다
                return False
            stack.pop() # 안비어있다면 스택에서 하나 빼주기

    return not stack # 스택이 비었는가?