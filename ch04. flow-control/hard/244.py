# 지그재그 숫자 삼각형을 출력
n = int(input())
num = 1

# n개의 행 출력
for row in range(1, n + 1):
    minus_num = 0
    # row번째 행에는 row개의 숫자가 있음
    for count in range(row):
        # 홀수 행은 왼쪽에서 오른쪽으로 출력
        if row % 2 != 0:
            print(num, end=" ")
            num += 1        
        # 짝수 행은 역순으로 출력
        else:
            print((num + row) - minus_num - 1, end=" ")
            minus_num += 2
            num += 1
    # 줄바꿈
    print()