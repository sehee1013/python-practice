# 교대 수열의 N항까지 누적 합을 출력하세요.
N = int(input())
total = 0
sign = 1

# 1부터 N까지 반복
for num in range(1, N + 1):
    
    # sign / i 반복
    term = sign / num

    # total에 더하기
    total += term
    
    # 다음 항에선 부호 바뀌게 하기
    sign *= -1
    
    # 결과 출력
    print(f"{num}항까지의 합: {total:.4f}")