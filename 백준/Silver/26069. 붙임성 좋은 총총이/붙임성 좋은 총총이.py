import sys
readline = sys.stdin.readline

# 붙임성 좋은 총총이
li = {"ChongChong"}

n = int(readline())
for _ in range(n):
    a, b = readline().strip().split()
    if a in li: li.add(b)
    elif b in li: li.add(a)
    
print(len(li))