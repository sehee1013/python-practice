# 1부터 N 사이에서 모든 자릿수가 동일한 수를 출력하세요.
N = int(input())

# 1부터 N까지 반복
for num in range(1, N + 1):
    
    # num을 문자열로 바꾸기
    str_num = str(num)

    first_digit = str_num[0]

    # 문자열 중 처음 문자와 다른 게 있으면 False
    found = all(digit == first_digit for digit in str_num)

    # True인 경우만 출력
    if found:
        print(num)