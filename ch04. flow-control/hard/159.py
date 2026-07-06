# 절대값은 if로 직접 계산하세요. chance 변수로 시도 횟수 추적
answer = 7
max_chance = 3
chance = 0

# 룰렛 판 출력
print("=== 행운의 룰렛 ===")
print(f"1~10 중 숫자를 맞춰보세요! (기회: {max_chance}번)")
# 빈 줄 출력으로 시각적 구분
print()

while True:
    # 3번 모두 실패 시 종료 메시지ㅣ 출력 후 종료
    if max_chance - chance == 0:
        print(f"기회를 모두 사용했습니다. 정답은 {answer}이었습니다.")
        break
    else:
        # 숫자 입력 받기
        guess_num = int(input())
        chance += 1
        # 정답이면 축하 메시지 출력 후 종료
        if guess_num == answer:
            print("정답입니다! 축하합니다!")
            break
        # 차이 절대값 1: 아주 가까워요! (뜨거워!) 남은 기회 횟수 출력
        elif abs(guess_num - answer) == 1:
            print(f"아주 가까워요! (뜨거워!) (남은 기회: {max_chance - chance}번)") 
        # 차이 절대값 2~3: 가까워요! (따뜻해요) 남은 기회 횟수 출력
        elif abs(guess_num - answer) <= 3:
            print(f"가까워요! (따뜻해요) (남은 기회: {max_chance - chance}번)") 
        # 차이 절대값 4 이상: 멀어요 (차가워요) 남은 기회 횟수 출력
        else:
            print(f"멀어요... (차가워요) (남은 기회: {max_chance - chance}번)")