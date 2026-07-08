# 한 줄에 이어 출력하려면 번호 카운터 변수를 따로 두고, 한 항목 출력 후 공백을 붙이세요.
text = input()

# 문자열 각 문자 순회하며 인덱스 부여하며 리스트 저장
result = [f"{idx + 1}.{char}" for idx, char in enumerate(text)]

# 결과 공백 구분하여 출력
print(" ".join(result))