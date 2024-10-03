# 인사성 밝은 곰곰이 
cnt = 0
li = set()

n = int(input())
for _ in range(n):
    name = input()
    if name == "ENTER":
        li = set()
    elif not(name in li):
        li.add(name)
        cnt+=1
    
print(cnt)