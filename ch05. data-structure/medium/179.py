# 각 문자에 대해 `c.lower() in "aeiou"`, `c.isalpha()`, `c.isdigit()` 같은 메서드로 분기.
s = input().lower()
vowel_count = 0
consonant_count = 0
number_count = 0

for char in s:
    # 모음인 경우 count + 1
    if char in "aeiou":
        vowel_count += 1
    # 숫자인 경우 count + 1
    elif char.isdigit():
        number_count += 1
    # 자음인 경우 count + 1
    elif char.isalpha():
        consonant_count += 1

# 결과 출력
print(f"모음: {vowel_count}")
print(f"자음: {consonant_count}")
print(f"숫자: {number_count}")