# %(나머지) 연산자와 if/else를 사용해 홀짝을 판별하세요.
num = int(input())

# num이 짝수인 경우 "num은(는) 짝수입니다" 출력
if num % 2 == 0:
  print(f"{num}은(는) 짝수입니다")
# num이 홀수인 경우 "num은(는) 홀수입니다" 출력
else:
  print(f"{num}은(는) 홀수입니다")