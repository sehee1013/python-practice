# 0번째부터 N번째 피보나치 수를 출력하세요.
n = int(input())
fibonacci = []

# 0번째 1번째 행 각각의 값은 0, 1로 설정
if n == 0:
    fibonacci = [0]
else:
    fibonacci = [0, 1]
# 2부터 n + 1 번째 행 값 구해서 리스트 추가  
for i in range(2, n + 1):
    fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
# 피보나치 수열 출력
print(f"피보나치 수열 (0~{n}번째):\n{' '.join(map(str, fibonacci)) + ' '}")