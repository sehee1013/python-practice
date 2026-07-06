s = input()
left_count = 0
right_count = 0

# 문자열 순회
for char in s:
    # 문자열이 "("인 경우 count + 1
    if char == "(":
        left_count += 1
    # 문자열이 ")"인 경우 count + 1
    elif char == ")":
        right_count += 1

# 두 count의 개수가 맞으면 올바름 출력
if left_count == right_count:
    print("올바름")
# 두 count의 개수가 맞지 않으면 올바르지 않음 출력
else:
    print("올바르지 않음")