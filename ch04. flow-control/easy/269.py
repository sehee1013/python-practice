# 발견 여부를 추적하는 플래그 변수를 사용합니다. 조건을 만족하는 첫 원소에서 break.
nums = [4, 7, 15, 3, 22, 9]
k = int(input())
found = False

# 리스트 순회:
for index, num in enumerate(nums):

    # k 이상인 값의 인덱스와 값 출력
    if num >= k:
        print(f"위치: {index}")
        print(f"값: {num}")
        found = True
        break

# 없으면 못 찾음
if not found:
    print("찾지 못했습니다")