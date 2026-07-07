# N개 정수 중 서로 다른 위치의 두 수 곱이 최대인 값을 구하세요.
n = int(input())
nums = []

nums = input().split()

max_num = -9999

# 리스트의 숫자 순환
for idx1, num1 in enumerate(nums):
    
    # 본인 제외 리스트 숫자랑 곱한 수가 max보다 크면 갱신
    for idx2, num2 in enumerate(nums):
        multiple = int(num1) * int(num2)
        if idx1 != idx2 and multiple > max_num:
            max_num = multiple

# 결과 출력
print(max_num)