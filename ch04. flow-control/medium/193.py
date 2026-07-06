s = input()
upper = 0
lower = 0
digit = 0
other = 0

# 문자 종류 따라 count + 1
for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
    else:
        other += 1

# 결과 출력
print(f"대문자: {upper}")
print(f"소문자: {lower}")
print(f"숫자: {digit}")
print(f"기타: {other}")