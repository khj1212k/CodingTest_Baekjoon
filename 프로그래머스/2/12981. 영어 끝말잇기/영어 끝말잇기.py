def solution(n, words):
    used_li = [] 
    prev = ''
    
    for i, wrd in enumerate(words):
        if i > 0:
            if wrd in used_li: # 이미 나온 단어
                return [(i%n)+1, (i//n)+1]
            if used_li[-1][-1] != wrd[0]:   # 틀린 단어
                return[(i%n)+1, (i//n)+1]
        used_li.append(wrd)
        
    return [0,0]