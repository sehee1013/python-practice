n = int(input())

# 행과 열의 숫자가 같은 경우, 또는 행과 열을 더한 값이 n - 1과 같은 경우 "*" 출력해서 대각선 만들기. 그 외는 공백 처리
for i in range(n):
    print(''.join('*' if (i==j or i+j==n-1) else ' ' for j in range(n)))