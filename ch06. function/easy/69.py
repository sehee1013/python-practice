# 첫 줄은 문자열, 둘째 줄은 정수입니다. 예: "ab" 와 3 → s="ab", n=3
s = input()
n = int(input())

# 함수 정의하기
def repeat(s, n):
    """문자열 s를 n번 이어 붙인 문자열 반환하기"""
    return s * n

# 함수 호출 후 출력
print(repeat(s, n))