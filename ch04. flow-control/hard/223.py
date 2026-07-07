# 누적합으로 삼각수를 구하고, 전체 합도 함께 누적
n = int(input())
triangula_num = 0
total = 0

# 1부터 n번째까지 출력 반복
for num in range(1, n + 1):
    # 각 삼각수 출력
    triangula_num += num
    print(f"T({num}) = {triangula_num}")
    
    # 합계 구하기
    total += triangula_num

# 합계 출력하기
print(f"합계: {total}")