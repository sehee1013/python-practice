# 빈 dict `borrowed` 에 책→사용자 누적 저장 → books 리스트 순회로 출력.
books = ["python", "java", "ruby", "go"]
n = int(input())
borrowed = {}

# 책, 사용자 형식으로 n번 입력 받기
# 같은 책에 대해 마지막으로 입력된 사용자가 현재 대출자
for _ in range(n):
    book, name = input().split(',')
    borrowed[book] = name

# 책 목록 순서대로 '책: 대출자' 형식으로 출력
# 대출되지 않은 책은 (없음)으로 표시
for book in books:
    print(f"{book}: {borrowed.get(book, '(없음)')}")