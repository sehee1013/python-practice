num = int(input())

# 원본 값 따로 저장
num_origin = num
count = 0

# num이 0보다 큰 동안 반복
while num > 0:
    # num에 num을 10으로 나눈 값 대입. 그때마다 count +1
    num //= 10
    count += 1

# 자릿수 출력
print(f"{num_origin}은(는) {count}자리 수입니다.")