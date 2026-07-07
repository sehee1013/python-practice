# 각 자릿수를 분리하여 한글로 변환하세요.
num = int(input())
result = ""

# 자릿수 한글
digits = {
    1:"일",
    2:"이",
    3:"삼",
    4:"사",
    5:"오",
    6:"육",
    7:"칠",
    8:"팔",
    9:"구",
}

# num이 0이 될 때까지 반복
while num > 0:
    
    # 4자리 수일 때
    if num >= 1000:
        # 몫이 1이 아닌 경우만 숫자 한글 넣기
        if num // 1000 != 1:        
            result += digits[num // 1000]
        
        result += "천"
    
        num %= 1000

    # 3자리 수일 때
    elif num >= 100:
        if num // 100 != 1:
            result += digits[num // 100]
        
        num %= 100
        result += "백"

    # 2자리 수일 때
    elif num >= 10:
        if num // 10 != 1:
            result += digits[num // 10]

        num %= 10 
        result += "십"

    # 1자리 수일 때
    else:
        result += digits[num]
        break

print(result)