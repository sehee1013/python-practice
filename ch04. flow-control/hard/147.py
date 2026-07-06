n = int(input())

# 행 n번 출력
for row in range(n):
    # 리스트 초기화
    nums = []
    # 열 n번 출력
    for col in range(n):
        # 출력할 숫자 계산하기
        num = min(row, col, n - 1 - row, n - 1 - col) + 1
        nums.append(num)
        
    # 공백 구분하여 한 줄에 출력
    print(" ".join(map(str, nums)))