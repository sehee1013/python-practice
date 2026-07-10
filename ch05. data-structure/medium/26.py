data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
k = int(input())

# k칸씩 건너뛰어서 리스트에 저장
result = data[::k]
# 리스트 공백 구분으로 출력
print(" ".join(map(str, result)))