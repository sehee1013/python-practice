data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
start = int(input())
end = int(input())

# 리스트 슬라이스 하고 공백 구분해서 역순으로 출력
print(" ".join(map(str, data[start:end][::-1])))