text = input()

# text 안의 문자 선택해서 반복
for char in text:

    count = 0

    # char이 text 안에 몇 개 있는지 세기
    for same_char in text:

        if char == same_char:
            count += 1

    # 결과 출력
    print(f"{char}: {count}개")