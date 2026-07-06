s = input()
result = ""

# 플래그
is_upper = True

# s 문자열 문자 하나씩 순회
for char in s:
    
    # 공백 찾으면 플래그 재변환
    if char == " ":
        result += char
        is_upper = True
    elif is_upper:
        # upper로 변환 후 플래그 변환
        result += char.upper()
        is_upper = False
    else:
        result += char

print(result)