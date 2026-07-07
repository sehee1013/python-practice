num = int(input())
ten_to_oct = ""

# n이 8보다 작아질 때까지 반복
while True:

    # num이 8보다 작을 때 그 값을 문자열에 넣어줌
    if num < 8:
        ten_to_oct += str(num)
        break

    else:
        # num % 8 문자열 형변환 후 ten_to_oct에 넣기
        digit = str(num % 8)
        ten_to_oct += digit
        
        # num = num // 8
        num = num // 8


# 문자열 뒤집어서 8진수 표현하기
print(ten_to_oct[::-1])