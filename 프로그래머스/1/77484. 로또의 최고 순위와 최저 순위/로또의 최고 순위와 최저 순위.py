def solution(lottos, win_nums):
    zeros = lottos.count(0)
    cnt = sum([1 for l in lottos if l in win_nums])
        
    rank1 = 7-cnt if cnt != 0 else 6
    rank2 = 7-(cnt+zeros) if (cnt+zeros) != 0 else 6
    answer = [rank2, rank1]
    return answer