text = input()
result = []

# text 반복
for char in text:

    # 알파벳인 경우 모듈러 연산
    if char.isupper():
        
        new_char = (ord(char) - ord('A') + 1) % 26 + ord('A')
    elif char.islower():
        new_char = (ord(char) - ord('a') + 1) % 26 + ord('a')
    # 그 외: 그대로 대입
    else:
        result.append(char)
        continue

    # 변환 후 문자열 추가
    result.append(chr(new_char))

print("암호:", "".join(result))