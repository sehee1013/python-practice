# N을 입력받아 1~N*N 숫자를 N열씩 탭 구분으로 출력하세요.
n = int(input())
num = 1

# n개의 행 출력
for row in range(n):
    num_list = []

    # n개의 열 생성
    for col in range(n):
        num_list.append(num)
        num += 1
        
    # 행 출력
    print(("\t".join(map(str, num_list))))