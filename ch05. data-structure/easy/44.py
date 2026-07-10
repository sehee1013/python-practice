# 문자열 변환 후 len 으로 자릿수 산출.
data_sets = [
    [1, 23, 456, 7890, 5, 100, 9999],
    [1, 5, 9],
    [10000],
]
t = int(input())
nums = data_sets[t]

# 문자열 길이 반환 후 리스트에 저장
result = [len(str(num)) for num in nums]

# 언패킹 사용하여 결과 리스트 출력
print(*result)