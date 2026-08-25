# 전역 total, count 시작값 0. 처리할 정수들을 리스트로 읽습니다. 예: "10 20 30" → nums=[10, 20, 30]
nums = [int(x) for x in input().split()]
total = 0
count = 0

# 함수 정의하기
def record(n):
    """전역 total에는 n을 더하고 전역 count는 1 늘리기"""
    # global 선언
    global total, count
    total += n 
    count += 1    

# nums 순회하며 record() 호출
for n in nums:
    record(n)
    
# 전역 total 출력
print(total)
# 전역 count 출력
print(count)