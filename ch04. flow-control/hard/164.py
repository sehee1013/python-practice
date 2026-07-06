# 3개 문장을 라운드별로 처리하세요.
text1 = "Hello Python"
text2 = "I love coding"
text3 = "Practice makes perfect"
total_correct = 0
total_chars = 0
round_num = 1

texts = [text1, text2, text3]

# 시작 시 출력 문장
print("=== 타자 연습 ===")
print("표시된 문장을 정확히 입력하세요!")
print()

# 3번 문장 입력 받기
for turn in range(3):
    correct = 0
    input_text = input()
    chars = len(texts[turn])
    
    # 인덱스 번호 turn의 text 가져와서 비교하기
    # 글자 수가 같으면 정확도 판별
    if len(input_text) == chars:

        # 0부터 문자열 길이까지 각각 인덱스의 문자 비교하기
        for idx in range(chars):
            if input_text[idx] == texts[turn][idx]:
                correct += 1
    else:
        continue
    
    # 정확도 계산
    accuracy = (correct / chars) * 100

    # 결과 출력
    print(f"[{round_num}번 문장] {texts[turn]}")
    print(f"정확도: {int(accuracy * 10) / 10}% ({correct}/{chars} 글자)")
    print()

    # 전체 값 갱신
    total_correct += correct
    total_chars += chars
    round_num += 1

# 전체 정확도 계산
total_accuracy = (total_correct / total_chars) * 100

# 최종 결과 출력
print("=== 최종 결과 ===")
print(f"전체 정확도: {int(total_accuracy * 10) / 10}% ({total_correct}/{total_chars} 글자)")