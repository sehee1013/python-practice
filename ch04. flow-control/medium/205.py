# 홀수 N을 입력받아 마름모를 출력하세요.
num = int(input())

# 전략: 가운데 행 기준으로 삼각형, 역삼각형 출력
# 삼각형: 공백 출력, "*" 출력
for star in range(1, num + 1, 2):
    empty = (num - star) // 2
    print(" " * empty + "*" * star)
# 역삼각형: 공백 출력, "*" 출력
for star in range(num - 2, 0, -2):
    empty = (num - star) // 2
    print(" " * empty + "*" * star)