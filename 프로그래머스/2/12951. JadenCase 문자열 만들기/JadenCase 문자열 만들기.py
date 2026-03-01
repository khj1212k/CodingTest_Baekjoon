def solution(s):
    
    return s[0].upper() + ''.join([s[i+1].upper() if s[i]==' ' and s[i+1]!=' ' else s[i+1].lower() for i in range(len(s)-1)])
