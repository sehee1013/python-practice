# N명에 대해 이름, 상태를 반복 입력받아 분류
n = int(input())
present = 0
absent = 0

# 이름, 상태 N번 받을 때까지 반복
for _ in range(n):
    
    # 이름, 상태 입력 받기
    name = input()
    attendance = int(input())

    # 상태 1이면 출석
    if attendance == 1:
        present += 1
        print(f"{name} - 출석")
    # 상태 0이면 결석
    elif attendance == 0:
        absent += 1
        print(f"{name} - 결석")

# 결과 출력
print("--- 출석 결과 ---")
print("출석:", present, "명")
print("결석:", absent, "명")