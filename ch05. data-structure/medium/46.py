# min, max 를 먼저 구해두고 컴프리헨션 안에서 사용하세요. 각 값을 f-string의 `:.2f` 로 포맷.
data = [10, 20, 30, 40, 50, 60, 70, 80]
n = int(input())

subset = data[:n]

# min, max 구하기
data_min = min(subset)
data_max = max(subset)
            
# 정규화해서 리스트 추가
results = [f"{(num - data_min) / (data_max - data_min):.2f}" for num in subset]

# 결과 출력
print(" ".join(map(str, results)))