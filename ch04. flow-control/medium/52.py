# for 반복문으로 1에서 20 중 3의 배수는 출력 넘어가기
for i in range(1, 20 +1):
    if i % 3 == 0:
        continue
    print(i) 