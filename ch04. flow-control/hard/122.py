# 1!부터 N!까지 출력하고 합을 구하세요.
n = int(input())
factorial_dict = {}

# 1!부터 n!까지 각각의 팩토리얼 값 구해서 출력, 딕셔너리 추가
current_factorial = 1
for i in range(1, n + 1):
    current_factorial *= i
    factorial_dict[f"{i}!"] = current_factorial

for key, value in factorial_dict.items():
    print(f"{key} = {value}")

# 전체 합 구해서 출력
print(f"{' + '.join(factorial_dict.keys())} = {sum(factorial_dict.values())}")