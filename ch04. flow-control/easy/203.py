# 정수를 이진수로 변환하여 1의 개수를 출력하세요. (bin() 사용 금지)
n = int(input())
one_count = 0

# n 복사한 copy_num 변수 선언
copy_num = n

# copy_num // 2의 값이 0 보다 클 때까지 반복
while copy_num > 0:
    # 2로 나눈 값이 1이면 one_count + 1
    if copy_num % 2 == 1:
        one_count += 1

    # copy_num 값 갱신
    copy_num //= 2

# 결과 출력
print(one_count)