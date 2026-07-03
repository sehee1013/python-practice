num = int(input())
reverse = 0

# num이 0보다 클 경우 반복
while num > 0:
    # num을 10으로 나누고 그 나머지 값을 리버스에 대입
    digit = num % 10
    reverse = reverse * 10 + digit

    # num은 10으로 나눈 몫을 대입
    num //= 10

# reverse 출력
print(f"뒤집은 숫자: {reverse}")