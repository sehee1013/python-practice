# 유클리드 호제법으로 GCD를 구하세요.
dividend = int(input())
divisor = int(input())

# 정수 2개를 입력받아 각각 divisor(제수)와 dividend(피제수)로 함.
# 나눗셈의 나머지는 다음 차례에서 제수가 되고, 원래 제수는 피제수가 됨을 반복
# 나머지가 0이 됐을 때, 그 때의 제수가 최대공약수


print(f"GCD({dividend}, {divisor}) 계산 과정:")

while True:
    remainder = dividend % divisor
    print(f"  {dividend} ÷ {divisor} = {dividend // divisor} ... 나머지 {remainder}")
    if remainder == 0:
        break
    dividend = divisor
    divisor = remainder 
    
# 나머지가 0이면 그때 divisor가 최대공약수
print(f"최대공약수: {divisor}")  