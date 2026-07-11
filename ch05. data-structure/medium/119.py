s = input()

# 입력 받은 문자열 앞뒤 공백 제거, 소문자로 변환, 공백은 _로 치환하여 출력
print(s.strip().lower().replace(" ", "_"))