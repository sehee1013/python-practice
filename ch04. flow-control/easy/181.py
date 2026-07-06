# 시작단과 끝단을 입력받아 해당 범위의 구구단을 출력하세요.
start = int(input())
end = int(input())

# start부터 end까지 반복
for dan in range(start, end + 1):
    # 단 시작 구분선 출력
    print(f"--- {dan}단 ---")
    # 1부터 9까지 출력 반복
    for digit in range(1, 10):
        print(f"{dan} x {digit} = {dan * digit}")