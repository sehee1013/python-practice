allowed = {"apple", "banana", "cherry", "date", "fig"}
n = int(input())
fruits = []

# n번 입력 받기
for _ in range(n):
    fruits.append(input())

# 입력 받은 것 중 allowed에 없는 것 구하기
not_allowed = set(fruits) - allowed

# 결과 출력
if not_allowed:
    print("미포함:", *sorted(not_allowed))
else:
    print("모두 포함")