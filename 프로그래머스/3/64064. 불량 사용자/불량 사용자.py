import re

def solution(user_id, banned_id):
    li = []
    results = set()
    
    for bid in banned_id:
        # print(banned_id[i])
        p = re.compile(bid.replace('*','.'))
        temp = []
        
        for uid in user_id:
            # print(p.fullmatch(uid))
            if p.fullmatch(uid): 
                temp.append(uid)
        li.append(temp)
        
    def dfs(idx, answer):
        if idx == len(li):
            results.add(frozenset(answer))
            return

        for i in li[idx]:
            if i not in answer:
                dfs(idx+1, answer + [i])
    
    dfs(0, [])
    return len(results)