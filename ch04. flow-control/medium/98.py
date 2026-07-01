start = int(input())
end = int(input())
total = 0
even_sum = 0

# start부터 end까지 반복
for num in range(start, end + 1):
    # 짝수인 경우 even_sum에 더하기
    if num % 2 == 0:
        even_sum += num
    # 전체 합 구하기
    total += num

# 결과 출력
print("구간 합계:", total)
print("짝수 합계:", even_sum)