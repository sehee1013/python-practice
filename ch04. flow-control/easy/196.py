s = input()
result = ""
vowels = "aeiouAEIOU"

for char in s:
    # 모음이 아니면 result에 추가
    if char not in vowels:
        result += char

# 결과 출력
print(result)