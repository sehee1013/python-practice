# 흐름: 입력 읽기 -> 함수 호출 -> 함수 실행 결과 출력
parts = input().split()
title = parts[0]
values = [int(x) for x in parts[1:-1]]
unit = parts[-1]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def report(title, *values, unit):
    s = 0
    for v in values:
        s += v
    return title + ": " + str(s) + unit

# 함수 호출하여 실행 결과 출력
print(report(title, *values, unit=unit))