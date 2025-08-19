def solution(s):
    jaden_case = []
    is_new_word = True
    
    for char in s:
        if char == ' ':
            jaden_case.append(' ')
            is_new_word = True
        else:
            if is_new_word:
                jaden_case.append(char.upper())
                is_new_word = False
            else:
                jaden_case.append(char.lower())
    
    return "".join(jaden_case)