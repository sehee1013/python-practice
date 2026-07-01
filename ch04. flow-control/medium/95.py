num = int(input())
total = 0

# 1부터 num-1까지의 약수 구하기
for divisor in range(1, num):
    # 구한 약수 total에 더하기
    if num % divisor == 0:
        total += divisor

# total값 출력
print(f"{num}의 약수의 합: {total}")

# total과 num이 같으면 완전수
if total == num:
    print(f"{num}은(는) 완전수입니다!")
# 그렇지 않으면 완전수 아님  
else:
    print(f"{num}은(는) 완전수가 아닙니다.")