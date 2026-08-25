# 전역 total, peak 시작값 0. 변화량들을 순서대로 읽습니다. 예: "5 -3 10" → parts=["5","-3","10"]
parts = input().split()
total = 0
peak = 0

# 함수 정의하기
def step(delta):
    """변화량 delta를 받아 전역 total 에 더하고, 만약 total 이 peak 보다 커지면 peak 도 갱신"""
    # global 선언
    global total, peak
    total += delta
    if total > peak:
        peak = total

# parts 순회하며 step() 호출
for delta in parts:
    step(int(delta))

# total, peak 출력
print(total)
print(peak)