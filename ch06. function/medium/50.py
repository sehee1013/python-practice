# 전역 positive_count 시작값 0. 검사할 정수들을 리스트로 읽습니다. 예: "1 -2 3" → nums=[1, -2, 3]
nums = [int(x) for x in input().split()]
positive_count = 0

# 함수 정의하기
def check(n):
    """n이 양수일 때만 전역 positive_count를 1 늘리기"""
    # positive_count를 global 선언하기
    global positive_count
    # n이 양수인 경우 + 1
    if n > 0:
        positive_count += 1

# nums 순회하면서 n 판별하기
for n in nums:
    # 함수 호출
    check(n)

# positive_count 출력
print(positive_count)