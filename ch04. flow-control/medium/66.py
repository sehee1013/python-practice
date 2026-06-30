# 위쪽 삼각형과 아래쪽 역삼각형을 각각 for문으로 출력하세요.
n = int(input())

# "*" 최대 출력 개수
max_star = (n * 2) - 1

# 가운데 행 중심으로 위쪽 삼각형 출력, 아래쪽 역삼각형 출력
for star_count in range(1, max_star, 2):
    space_count = ((max_star) - star_count) // 2
    print(" " * space_count + "*" * star_count)

for star_count in range(max_star, 0, -2):
    space_count = ((max_star) - star_count) // 2
    print(" " * space_count + "*" * star_count)