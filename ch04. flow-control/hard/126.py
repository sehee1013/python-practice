print("3자리 암스트롱 수:")

# 100부터 999까지 반복
for num in range(100, 1000):
    # num 문자열로 변환하고 각각 인덱스 순서대로 변수 선언
    str_num = str(num)
    
    # 각각 자릿수의 세제곱 값을 더한 값이 같으면 출력
    hundred_digit = str_num[0]
    ten_digit = str_num[1]
    one_digit = str_num[2]

    total = int(hundred_digit) ** 3 + int(ten_digit) ** 3 + int(one_digit) ** 3
    
    # num과 total이 같으면 결과 출력
    if num == total:
        print(f"{num} = {hundred_digit}^3 + {ten_digit}^3 + {one_digit}^3")