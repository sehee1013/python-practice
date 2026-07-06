# 이중 반복문과 배치 카운트로 구현하세요.
n = int(input())
m = int(input())
total_row = 0

# 행 출력할 때까지 반복
for row in range(1, n // m + 1):
    # 행 번호 출력 
    print(f"[{row}행]", end=" ")
    # m열 출력할 때까지 반복
    for col in range(1, m + 1):
        print(f"{row}-{col}", end="  ")
    total_row += 1
    # 줄바꿈 해주기
    print()
    
# n % m != 0이면
if n % m != 0:
    # n // m + 1행 출력
    print(f"[{n // m + 1}행]",end=" ") 
    # n % m열까지 출력
    for col in range(1, n % m + 1):
        print(f"{n // m + 1}-{col}", end="  ") 
    total_row += 1
    print()
# 총 결과 출력 
print(f"총 {total_row}행 배치 완료 ({n}명)")