def solution(s):
    answer = []
    s = [li.split(',') for li in s[2:-2].split('},{')]
    s.sort(key=lambda x : len(x))
    
    for li in s:
        for n in li:
            if n not in answer:
                answer.append(n)
                break
    return list(map(int, answer))