# 카운터로 정렬하고, 갯수가 많은것부터 한세트씩 박스에 넣는다. 
# 만약 summ+v가 박스크기보다 크면, 그 v는 패스하고 다음세트는 들어가는지 확인
# 이렇게 for을 끝까지

from collections import Counter

def solution(k, tangerine):
    c = Counter(tangerine).most_common()
    cnt = 0
    summ = 0
    for _,v in c:
        if summ >= k:
            break
        summ+=v
        cnt+=1
    return cnt