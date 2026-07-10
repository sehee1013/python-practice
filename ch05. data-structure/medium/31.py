data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = int(input())

# k = 0인 경우, 그대로 출력
if k == 0:
    print(" ".join(map(str, data)))
# 제거한 가운데 부분만 공백 구분하여 출력하기
else:
    print(" ".join(map(str, data[k:-k])))