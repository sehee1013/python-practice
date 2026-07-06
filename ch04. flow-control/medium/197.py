s = input()
result = []
is_upper = False

# 문자열 s의 문자 하나씩 순회
for char in s:
    
    # 문자가 "_"인 경우
    if char == "_":
        is_upper = True
    # is_upper인 경우
    elif is_upper:
        # 대문자로 리스트 저장 is_upper = False
        result.append(char.upper())
        is_upper = False
    # 그 외는 그대로 리스트 저장
    else:
        result.append(char)

# 결과 출력
print("".join(result))