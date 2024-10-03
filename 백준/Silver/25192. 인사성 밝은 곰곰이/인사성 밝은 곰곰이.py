import sys

cnt = 0
li = set()

# 전체 입력을 한 번에 처리
n = int(sys.stdin.readline())
for _ in range(n):
    name = sys.stdin.readline().strip()  # 입력값의 개행 문자를 제거
    if name == "ENTER":
        li.clear()  # 재할당 대신 set을 비우는 방법
    elif name not in li:
        li.add(name)
        cnt += 1

print(cnt)