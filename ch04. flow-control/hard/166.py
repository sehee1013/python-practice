# 정답 42. prev_diff=100 초기값.
treasure = 42
attempt = 0
prev_diff = 100

# 시작 출력
print("=== 보물 찾기 ===")
print("1~100 사이에 보물이 숨겨져 있습니다!")
print()

# 찾을 때까지 반복
while True:
    # 값 입력 받기
    guess_num = int(input())
    attempt += 1
    # 값이 42보다 큰 경우
    if guess_num > 42:
        diff = guess_num - 42
    # 아닌 경우
    else:
        diff = 42 - guess_num

    # 정답인 경우, 메시지 출력 후 종료
    if diff == 0:
        print(f"보물을 찾았습니다! (시도: {attempt}회)")
        print(f"축하합니다! 총 {attempt}번 만에 보물을 찾았습니다!")
        break

    # 절대값 차이가 1~5인 경우 
    elif 1 <= diff <= 5:
        print(f"뜨거워! 아주 가까워요! (시도: {attempt}회)")

    # 절대값 차이가 6~15인 경우 
    elif 6 <= diff <= 15:
        print(f"따뜻해요! 근처에 있어요! (시도: {attempt}회)")

    # 절대값 차이가 16~30인 경우 
    elif 16 <= diff <= 30:
        print(f"미지근해요... (시도: {attempt}회)")
        
    # 절대값 차이가 >= 31인 경우 
    else:
        print(f"차가워요! 멀리 있어요! (시도: {attempt}회)")

    # 최근 절대값보다 작아졌으면 격려 메시지 출력
    if prev_diff > diff:
        print("점점 가까워지고 있어요!")

    # 최신 절대값 갱신
    prev_diff = diff