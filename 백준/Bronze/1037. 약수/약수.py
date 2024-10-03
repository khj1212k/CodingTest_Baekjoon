n = int(input())  # 진짜 약수의 개수
li = list(map(int, input().split()))  # 진짜 약수 리스트

# N 구하기
N = min(li) * max(li)

# 출력
print(N)