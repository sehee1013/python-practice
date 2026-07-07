# while로 자릿수 제곱합 반복, 시작값 재등장 시 순환으로 판단
original = int(input())

# 행복한 수 플래그
is_happy = False
to_happy_num = original
# original을 문자열로 바꾸기
to_happy_num_str = str(to_happy_num)
# 중복 확인용 set
seen = set()

# 최대 100번까지 반복
for tries in range(1, 101):

    # to_happy_num set에 넣기
    seen.add(to_happy_num)
    # to_happy_num 문자열로 바꾸기
    to_happy_num_str = str(to_happy_num) 
    # 각각 자릿수 제곱한 값 더하는 용도
    digit_total = 0

    # to_happy_num_str의 각각의 문자열 정수형으로 변환
    for digit_str in to_happy_num_str:

        digit = int(digit_str)
        # 자릿수 제곱하고 digit_total에 넣기
        digit_total += digit ** 2

    # 계산 과정 출력
    print(f"단계 {tries}: {to_happy_num} → {digit_total}")
    
    # 제곱합으로 위 과정 다시 반복
    to_happy_num = digit_total

    # to_happy_num == 1이면 종료 
    if to_happy_num == 1:
        is_happy = True
        break
    
    # 이미 나온 적 있는 수면 종료
    if to_happy_num in seen:
        break


# 결과 출력
if is_happy:
    print(f"{original}은(는) 행복한 수입니다!")
else:
    print(f"{original}은(는) 행복한 수가 아닙니다.")