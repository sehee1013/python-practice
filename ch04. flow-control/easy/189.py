# 문자열을 입력받아 같은 문자가 연속으로 가장 많이 반복된 횟수를 출력하세요.
s = input()
current_char = ""
current_count = 0
max_count = 0

# 문자열 끝날 때까지 한 문자씩 반복
for char in s:
    # current_char이랑 char이 같으면 + 1
    if current_char == char:
        current_count += 1
    # 다르면 current_count = 1, current_char에 char 대입
    else:
        current_char = char
        current_count = 1

    # 갯수 갱신
    max_count = max(current_count, max_count)

# 결과 출력
print(max_count)