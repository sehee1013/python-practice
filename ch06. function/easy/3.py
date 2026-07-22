# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "10 2" → a=10, b=2
a, b = [int(x) for x in input().split()]

# 두 정수를 비교하여 더 큰 값을 반환하는 함수 정의
def bigger(a, b):
    if a >= b:
        return a
    return b

# 함수 호출하여 결과 출력
print(bigger(a, b))