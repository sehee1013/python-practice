existing = {"윤서", "지우", "민준"}
n = int(input())

# n번 이름 입력 받고 set에 추가
for _ in range(n):
    name = input()
    existing.add(name)
    
# 고유 학생 수 출력
print(f"고유 학생 수: {len(existing)}")