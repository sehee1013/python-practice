# 바깥 for문은 단, 안쪽 for문은 곱하는 수(1~9)입니다.
start_dan, end_dan = map(int, input().split())

# 구구단 일부 출력
# 단 반복 출력
for dan in range(start_dan, end_dan + 1):
    # 단 시작선 출력하여 시각적 구분
    print(f"--- {dan}단 ---")
    # 곱셈 수 반복 출력
    for mul in range(1, 10):
        print(f"{dan} x {mul} = {dan * mul}")
    # 단 끝나면 빈 줄 한 줄 출력하여 다음 단과 시각적 구분. 마지막 단은 제외
    if dan != end_dan:
        print()