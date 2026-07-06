# 나비 모양 패턴을 출력하세요.
n = int(input())
center = (n + 1) // 2
total_width = 2 * n - 1

# 가운데 줄 기준으로 증가, 감소
# 위쪽
for row in range(1, center):
    inner_empty = total_width - (2 * row)
    print("*" * row + " " * inner_empty + "*" * row)

# 가운데 줄
print("*" * total_width)

# 아래쪽
for row in range(center - 1, 0, -1):
    inner_empty = total_width - (2 * row)
    print("*" * row + " " * inner_empty + "*" * row)