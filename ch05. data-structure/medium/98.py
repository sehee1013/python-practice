n = int(input())

seen = set()
found = False

# n번 입력 반복
for _ in range(n):
    input_value = input()
    # 처음 중복이면 출력하고 종료
    if input_value in seen:
        print(input_value)
        found = True
        break
    else:
        seen.add(input_value)

# 못 찾은 경우 메시지 출력
if not found:
    print("중복 없음")