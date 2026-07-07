# 첫 칸에서 마지막 칸까지 도달 가능 여부를 판별하세요.
n = int(input())

# n개의 점프력 입력 받아 공백 기준으로 구분하기
jumps = input().split()
target_idx = n - 1
max_reached = 0

# n번 반복
for idx in range(n): 

    # 도달 못하고 인덱스 넘어가면 종료
    if idx > max_reached:
        break
    
    # 최대 도달 수 갱신
    max_reached = max(max_reached, int(jumps[idx]) + idx)

    # 도달하면 종료
    if max_reached >= target_idx:
        break

# 결과 출력
if max_reached >= target_idx:
    print("YES")
else:
    print("NO")