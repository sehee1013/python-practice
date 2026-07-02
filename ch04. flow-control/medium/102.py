text = input().strip()

# 문자열 한 문장 끝날 때까지 반복
for char in text:
    # 문자열 하나씩 대분자로 출력 (줄바꿈X) 
    print(char.upper(), end="")
# 줄 바꿈
print()