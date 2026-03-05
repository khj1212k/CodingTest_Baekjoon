def solution(s):
    stack = []
    [stack.pop(-1) if stack and stack[-1] == char else stack.append(char) for char in s]
    return 0 if stack else 1