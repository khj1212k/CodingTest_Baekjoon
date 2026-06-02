def solution(word):
    words = []
    
    def dfs(current):
        if len(current) > 5:  return 
        
        words.append(current)
            
        for v in 'AEIOU':  dfs(current + v)
    
    dfs("")
    return words.index(word)