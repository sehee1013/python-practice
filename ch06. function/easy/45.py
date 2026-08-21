# 전역 count 시작값 0. 호출 횟수 n 을 입력에서 읽습니다. 예: "5" → n=5
count = 0
n = int(input())

# 함수 정의하기
def increase():
    """호출될 때마다 전역변수 count + 1"""
    # 전역변수 count global 선언
    global count
    # count + 1
    count += 1

# n번 increase() 실행
for _ in range(n):
    increase()

# count 출력
print(count)