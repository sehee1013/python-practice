# 전역 total 시작값 0. 더할 정수들을 리스트로 읽습니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
total = 0
nums = [int(x) for x in input().split()]

# 함수 정의하기
def add(n):
    # 전역변수 total global 선언
    global total
    # total에 누적하기
    total += n

# 함수 호출하고 실행 결과 출력
for n in nums:
    add(n)

print(total)