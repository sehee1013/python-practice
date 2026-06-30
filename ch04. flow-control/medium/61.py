# range(n, 0, -1)은 n부터 1까지 감소합니다.
n = int(input())

# 입력받은 값 n만큼 행 출력
# 첫 줄: 별 n개, 마지막 줄: 별 1개
for star in range(n, 0, -1):
    print("*" * star)