from collections import deque

def solution(begin, target, words):
    cnt = 0
    visited = []
    q = deque([(begin, cnt)])
    
    while q:
        cur_word, cur_cnt = q.popleft()
        for word in words:
            if sum(1 for i,j in zip(cur_word,word) if i!=j )==1 and word not in visited:
                if word == target : return cur_cnt+1
                q.append((word, cur_cnt+1))
                visited.append(word)
    
    return 0