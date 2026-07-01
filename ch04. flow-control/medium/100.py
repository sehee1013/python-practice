text = input()
count = 0

# 문자열 끝날 때까지 반복하면서 count + 1
for char in text:
    count += 1

# 결과 출력
print("문자열 길이:", count)