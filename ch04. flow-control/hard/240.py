n = int(input())

# n번째 행을 기준으로 증가, 감소
# 1행부터 n -1행까지 별 개수 증가
for up_arrow in range(1, n):
    # "*"을 공백 한 칸으로 연결
    print(" ".join("*" * up_arrow))
# n행부터 1행까지 별 개수 감소
for down_arrow in range(n, 0, -1):
    # "*"을 공백 한 칸으로 연결
    print(" ".join("*" * down_arrow))