# 온도를 입력받아 30도 초과이면 두 줄을 출력하세요.
temperature = int(input())

#온도가 30도 초과면 "폭염주의보", "외출을 자제하세요" 출력
if temperature > 30:
    print("폭염주의보")
    print("외출을 자제하세요")