# 초기값으로 max_d=0, pos=0 (또는 -1) 로 두고 strict greater(>) 일 때만 갱신해야 동률 처리가 맞습니다.
n = int(input())
# 최대 차와 인덱스 변수 선언
max_d = 0
max_idx = 0

# 일별 기온 n개 입력 받아 리스트 만들기
temps = [int(x) for x in input().split()]

# idx - (idx + 1)의 절대값 구하기
for idx in range(n - 1):
    # 기온차 변수 선언
    current_d = abs(temps[idx] - temps[idx + 1])
    # 기존 최대 차보다 크면 갱신
    if current_d > max_d:
        max_idx = idx
        max_d = current_d

# 최대 차와 위치 출력
print(f"최대 차: {max_d}")
print(f"위치: {max_idx} ~ {max_idx + 1}")