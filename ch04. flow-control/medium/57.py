"""
TITLE: 소수 판별
DIFFICULTY: medium
TAGS: for, break, prime, flag

EVAL: stdio

DESCRIPTION:
2 이상의 정수 N을 입력받아 소수인지 판별하시오.
- 2부터 N-1까지 나누어 떨어지는지 확인합니다.
- 나누어 떨어지는 수 i를 발견하면
  `N은(는) 소수가 아닙니다 (N = i x N//i)` 형식으로 출력하고 종료합니다.
- 끝까지 나누어 떨어지지 않으면 `N은(는) 소수입니다`를 출력합니다.

예시:
- 입력: `7` → 출력: `7은(는) 소수입니다`
- 입력: `12` → 출력: `12은(는) 소수가 아닙니다 (12 = 2 x 6)`
"""

# is_prime = True 로 시작, for i in range(2, num): 나누어지면 출력 + is_prime=False + break.
num = int(input())
is_prime = True
# 2 이상의 값 정수 N 입력 받아 소수 판단
# 1보단 크고 N 보다 작은 수로 나머지가 0이 될 때까지 계속 나누기 
for i in range(2, num):
  if num % i == 0:   # 나누어 떨어지는 수 발견하면 소수 아니라는 메시지 출력
    print(f"{num}은(는) 소수가 아닙니다 ({num} = {i} x {num // i})")
    is_prime = False
    break

# 발견 못하면 소수라는 메시지 출력
if is_prime:
  print(f"{num}은(는) 소수입니다")