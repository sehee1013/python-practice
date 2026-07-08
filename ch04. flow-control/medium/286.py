text = input()
result_char = []

#문자열 하나씩 검사
for idx, char in enumerate(text):

    # 인덱스 짝수면 글자 대문자
    if idx % 2 == 0:
        result_char.append(char.upper())

    # 인덱스 홀수면 글자 소문자
    else:
        result_char.append(char.lower())
    
# 변환 결과 리스트 문자열에 넣기
result = "".join(result_char)

# 결과 출력
print(result)