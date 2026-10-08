# 입력을 정수 리스트로 만듭니다. 예: "2 10" → nums=[2, 10]
nums = [int(x) for x in input().split()]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def power(base, exp):
    return base ** exp

# nums 를 * 로 풀어 power 에 넘기고, 그 반환값 출력
print(power(*nums))