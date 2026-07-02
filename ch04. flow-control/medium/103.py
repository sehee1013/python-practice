text = input()
result = ""

# 문자열 끝날 때까지 반복
for idx in range(len(text)-1, -1, -1):
    # 문자열 끝에서부터 인덱스 번호 이용하여 result에 대입
    result += text[idx]

# 결과 출력
print("뒤집은 문자열:", result)