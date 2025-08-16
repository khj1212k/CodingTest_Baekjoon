def solution(name, yearning, photo):
    dic = {k:v for k,v in zip(name,yearning)}
    return [sum(dic[n] for n in li if n in name) for li in photo]