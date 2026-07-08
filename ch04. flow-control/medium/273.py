# 누적합 변수와 발견 플래그를 둡니다.
# 한 원소를 살필 때 0이면 즉시 continue, 그 외에는 누적합에 더한 직후 K 도달 여부를 검사하세요.
# 반복문 종료 후 플래그로 "한계 미달" 여부를 판정합니다.
nums = [4, 0, 3, 0, 0, 7, 2, 0, 8, 1]
k = int(input())
total = 0
found = False

# nums 원소 하나씩 보기
for idx, num in enumerate(nums):
    # num == 0이면 인덱스 출력 후 넘어가기
    if num == 0:
        print(f"무시한 위치: {idx}")
        continue

    # 그 외는 total에 더함
    total += num
    
    # 누적합이 K 이상이 되는 순간 출력 후 종료
    if total >= k:
        print(f"종료 위치: {idx}")
        print(f"최종 누적합: {total}")
        found = True
        break

# 못 찾은 경우 출력
if not found:
    print(f"한계 미달, 누적합: {total}")