n = int(input())

# 입력 받은 n만큼 행과 열 출력. 행 + 열이 짝수면 "#" 출력
# (row + col) % 2 == 0인 경우 "#"출력. 그 외: "." 출력 (공백 구분자)
for row in range(n):
    print(" ".join('#' if (row + col) % 2 == 0 else '.' for col in range(n)))