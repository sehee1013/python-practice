n = int(input())

# n번 입력 반복
for row in range(1, n + 1):
    # 입력 받기
    words = input().split()

    # 개수 출력
    print(f"{row}줄: {len(words)}개")