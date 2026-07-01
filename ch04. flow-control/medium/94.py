# 1부터 num까지 반복하며 나머지가 0이면 약수
num = int(input())
count = 0

# 1부터 n까지 반복
for divisor in range(1, num + 1):
    # num을 나눴을 때의 나머지가 0인 경우 출력, count + 1
    if num % divisor == 0:
        print(divisor)
        count += 1
# 결과 출력
print("약수의 개수:", count)