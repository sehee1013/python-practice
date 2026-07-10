# 음수 인덱스도 슬라이스의 양 끝에 사용 가능합니다 — 끝에서부터의 위치를 의미합니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
start_idx = int(input())
end_idx = int(input())

# 음의 정수 인덱스로 슬라이스하여 정수 추출 후 출력
print(" ".join(map(str, data[start_idx:end_idx])))