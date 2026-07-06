# for문으로 순회하며 이전 문자와 현재 문자를 비교하세요.
s = input()

result = ""
current_char = ""
count = 0

# 문자열 s의 각 문자 순회
for char in s:
    # 이전 문자와 다르고 count > 0인 경우
    if current_char != char:
        # result에 이전 문자와 카운트 넣기
        if count > 0:
            # 이전 문자와 count는 문자열에 넣고
            result += current_char + str(count)

        # 현재 문자를 이전 문자로 갱신 , count = 1
        current_char = char
        count = 1

    # 이전 문자와 같으면
    else:
        # 카운트 + 1
        count += 1

# 마지막 문자와 카운트 입력 후 종료
if count > 0:
    result += current_char + str(count)

# 결과 출력
print(result)