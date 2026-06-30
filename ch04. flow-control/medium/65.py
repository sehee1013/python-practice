# range(i, 0, -1)로 i부터 1까지 역순 출력하세요.
num = int(input())

# num행 출력, 0번째 행 num부터 역순 출력
for row in range(num, 0, -1):
    for max_num in range(row, 0, -1):
        print(max_num, end="")
    print()