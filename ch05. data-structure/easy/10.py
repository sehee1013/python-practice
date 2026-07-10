# pop 의 반환값을 변수에 저장해두면 출력에 활용할 수 있습니다.
data_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["혼자"],
]
t = int(input())
applicants = data_sets[t]

# 명단 마지막 한 명 삭제 후 삭제한 이름 출력
print(f"취소된 사람: {applicants.pop()}")

remained = " ".join(applicants)

# 남은 명단 출력
print(f"남은 명단: {remained.rstrip()}")