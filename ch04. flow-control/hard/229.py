# 첫 줄에 N, 둘째 줄에 N개 정수를 입력받아 최대 연속 부분합을 구하세요.
n = int(input())
max_sum = -9999
current_sum = 0

# 정수 n개 입력 받고 공백 기준으로 분리하기
nums = input().split()

# 각 숫자 순회하며 더하기
for num in nums:
    
    # 정수형으로 변환
    int_num = int(num)

    # 최근 합에 int_num을 더한 것과 int_num 비교해서 더 큰 쪽을 갱신
    current_sum = max(int_num, current_sum + int_num)

    # 최근 합과 최대 합 비교하여 더 큰 쪽 갱신
    max_sum = max(max_sum, current_sum)

# 결과 출력
print(max_sum)