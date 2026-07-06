# 단가와 수량범위 N을 입력받아 가격표를 출력하세요.
price = int(input())
n = int(input())

# 1개부터 N개까지 가격표 한 줄씩 출력
for num in range(1, n + 1):
    print(f"{num} x {price} = {num * price}")