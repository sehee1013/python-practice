# N개 정수에서 연속으로 증가하는 가장 긴 구간의 길이를 구하세요.
n = int(input())
pre_num = -9999
count = 0
max_count = 0

# 정수 입력 받기
nums = input().split()

for num in nums:
    
    # num을 정수형으로 바꾸기
    int_num = int(num)

    # 이전 정수와 비교했을 때 더 큰 값이면 count + 1
    if int_num > pre_num:
        count += 1
        max_count = max(max_count, count)
    # 이전 정수보다 크지 않으면 count 리셋
    else:
        count = 1

    # 이전 정수 갱신
    pre_num = int_num

# 결과 출력
print(max_count)