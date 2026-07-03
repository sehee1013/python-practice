n = int(input())
total = 0
i = 1

#1부터 입력받은 숫자 N까지 반복해서 더해주기
while i <= n:
    total += i
    i += 1
    
print(f"1부터 {n}까지의 합: {total}")