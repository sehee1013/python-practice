r = int(input())
c = int(input())

# 행과 열 생성해서 좌표 생성 후 리스트 추가
result = [f"({row},{col})" for row in range(r) for col in range(c)]

# 결과 출력
print(*result)