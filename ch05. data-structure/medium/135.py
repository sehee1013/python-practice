# 5개 카운터 + if/elif 분기로 분류.
data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]

# 5개 카운터 변수 초기화
a = b = c = d = f = 0

# 점수 순회
for score in scores:
    # 점수 별 등급 판정
    if score >= 90:
        a += 1
    elif score >= 80:
        b += 1
    elif score >= 70:
        c += 1
    elif score >= 60:
        d += 1
    else:
        f += 1

# 결과 출력
print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")
print(f"D: {d}")
print(f"F: {f}")