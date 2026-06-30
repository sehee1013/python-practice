# for i in range(5): num = int(input()); if num % 2 != 0: print("홀수는 건너뜁니다"); continue; total += num
total = 0
# 정수 5개 한 줄씩 입력받아 홀수 건너뛰고 짝수만 합계 누적하기
for i in range(5):
    num = int(input()) 
    if num % 2 != 0: # 홀수면 건너뜀
        print("홀수는 건너뜁니다")
        continue
    total += num

# 짝수 합계 출력 
print("짝수 합계:", total)