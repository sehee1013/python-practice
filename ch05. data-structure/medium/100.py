allowed = {"apple", "banana", "cherry", "date", "fig"}
n = int(input())

# n번 검사 항목 입력 받기
items = {input() for _ in range(n)}

# 결과 출력
if items <= allowed:
    print("모두 포함")
else:
    print("미포함 있음")