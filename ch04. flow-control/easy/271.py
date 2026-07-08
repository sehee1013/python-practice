# 누적합 변수를 두고, K 이하인 원소는 continue로 건너뛰세요.
nums = [3, -2, 5, 0, -7, 4, -1, 6]
k = int(input())
total = 0

# nums의 요소 순회하며 판별
for num in nums:
    # k 이하인 값은 건너뛰기
    if num <= k:
        continue
    # 요소 total에 더하기
    total += num

# 결과 출력
print(f"합계: {total}")