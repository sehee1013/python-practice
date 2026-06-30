"""
TITLE: 숫자 맞추기 게임
DIFFICULTY: medium
TAGS: while, break, if-elif-else

EVAL: stdio

DESCRIPTION:
정답은 `42`입니다. 숫자를 반복해서 입력받아 정답과 비교합니다.
- 입력한 수가 정답보다 작으면 `더 큰 수를 입력하세요`
- 입력한 수가 정답보다 크면 `더 작은 수를 입력하세요`
- 정답이면 `정답입니다!`를 출력하고 종료합니다.

예시:
- 입력: `30\n50\n42` → 출력:
  ```
  더 큰 수를 입력하세요
  더 작은 수를 입력하세요
  정답입니다!
  ```
"""
# while True 안에서 정답일 때 break 하세요.
answer = 42

# while True 시작하기
while True:
    # 사용자 정답 받기 user_answer "숫자를 입력하세요: "
    user_answer = int(input())
    # 만약 입력한 수가 정답보다 작으면 "더 큰 수를 입력하세요" 출력
    if user_answer < answer:
        print("더 큰 수를 입력하세요")
    # 만약 입력한 수가 정답보다 크면 "더 작은 수를 입력하세요" 출력
    elif user_answer > answer:
        print("더 작은 수를 입력하세요")
    # 정답이면 "정답입니다!" 출력하고 종료
    else:
        print("정답입니다!")
        break