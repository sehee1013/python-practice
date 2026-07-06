s = input()
result = ""

# s 속 문자 순환
for char in s:

    if not char.isalpha():
        result += char
        continue

    unicode_char = ord(char)

    # 유니코드 변환 후 77 이상 or 109 이상이면 -13
    if 90 >= unicode_char >= 77 or 122>= unicode_char >= 109:
        result += chr(unicode_char - 13)
    # 그 외: 유니코드 변환 후 + 13 한 후 다시 문자로 변환
    elif 65 <= unicode_char <77 or 97 <= unicode_char < 109:
        result += chr(unicode_char + 13)

# 결과 출력
print(result)