# 1부터 100까지 반복
for num in range(1, 101):
    # num이 3과 5의 공배수일 때 한 줄씩 출력
    if num % 3 == 0 and num % 5 == 0:
        print(num)