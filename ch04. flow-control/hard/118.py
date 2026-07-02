# 2 이상의 정수를 입력받아 소수 여부를 판별하세요.
num = int(input())

# num이 num보다 작고 2 이상의 값으로 나누었을 때 나머지가 0인 게 있으면 소수가 아님
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print(f"{num}은(는) 소수가 아닙니다.")
        break
# 판별 결과 출력
else:
    print(f"{num}은(는) 소수입니다.")