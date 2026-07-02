text = input()
remove = input()
result = ""

# 문자열 끝날 때까지 반복
for char in text:
    # 문자가 remove랑 같지 않을 때 result에 더함
    if char != remove:
        result += char

# 결과 출력
print("결과:", result)