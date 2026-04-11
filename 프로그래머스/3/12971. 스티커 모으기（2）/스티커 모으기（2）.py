def dp_func(sticker):
    dp = [0] * len(sticker)
    
    for i in range(len(sticker)):
        if   i==0: dp[0] = sticker[0]
        elif i==1: dp[1] = max(dp[0], sticker[1])
        else     : dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
        
    return dp[-1]

def solution(sticker):
    return max(dp_func(sticker[1:]), dp_func(sticker[:-1])) if len(sticker) != 1 else sticker[0]
    
    