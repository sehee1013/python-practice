# 정수 리스트 변환 후 두 번째 줄에서 a, b 를 받아 del 슬라이싱 한 줄로 처리하세요.
n = int(input())

# n개의 정수 입력 받기
nums = [int(x) for x in input().split()]
# 정수 a, b 입력 받기
start_idx, end_idx = map(int, input().split())

# 인덱스 a 이상 b 미만 구간 삭제
del nums[start_idx:end_idx]

# 결과 출력
print(" ".join(map(str, nums)))