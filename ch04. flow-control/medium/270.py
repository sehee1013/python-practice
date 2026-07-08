# 누적합 변수와 발견 플래그를 두고, 매 원소를 더한 직후 K 초과 여부를 검사합니다.
nums = [3, 5, 2, 8, 1, 4, 6, 7]
k = int(input())
total = 0
found = False
# nums의 길이만큼 반복
for idx, num in enumerate(nums):
    # 원소 값 차례대로 total에 더하기
    total += num
    # total이 k를 초과할 때 종료
    if total > k:
        # 위치와 누적합 출력
        print(f"위치: {idx}")
        print(f"누적합: {total}")
        found = True
        break

# 발견하지 못한 경우 출력
if not found:
    print("한계 미달")