# yellow = (h-1) * (w-1)
# brown=2h+2w-4 -> b/2=h+w-2 -> h-1= b/2-w+1 -> w-1=b/2-h+1
# -> yellow = w-1(b/2-w+1) -> -ww(ww-b/2) -> b/2 = ww+y/ww -> ww*b/2 = ww^2+y

def solution(b, y):
    answer = []
    total = b+y
    
    for w in range(1, total): # width
        if total % w != 0: continue # 약수
        h = total // w # hight
        if (h-2)*(w-2) == y:
            return [h, w]
    
    return answer