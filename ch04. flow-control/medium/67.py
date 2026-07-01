n = int(input())

# 1부터 입력받은 값 n까지의 곱셈표 출력
# 헤더 출력, 구분선 출력, 1부터 n까지 곱셈값 출력
print("X", end="\t")

for header in range(1, n + 1):
    print(header, end="\t")
print()
# 구분선 출력하여 시각적 구분
print("-" * 30)

# 1부터 n까지 곱셈 결과 출력
for i in range(1, n + 1):
    print(i, end = "\t")
    for j in range(1, n + 1):
        print(i * j, end = "\t")
    print()