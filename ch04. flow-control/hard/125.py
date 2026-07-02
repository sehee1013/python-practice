# 10진수를 2진수로 직접 변환하세요.
num = int(input())
digit = num
turn = 0
result = 0

if num != 0:
    print("변환 과정:")

# 몫이 0이 될 때까지 반복
while digit != 0:

    # 각 나눗셈 단계 출력
    print(f"  {digit} ÷ 2 = {digit // 2} ... 나머지 {digit % 2}")
    
    # 나머지 값은 list에 추가
    result += digit % 2
    result *= 0.1

    # digit // 2의 값을 digit에 대입
    digit //= 2
    turn += 1

# 결과 출력
print(f"{num} → 2진수: {int(result * (10 ** turn))}")