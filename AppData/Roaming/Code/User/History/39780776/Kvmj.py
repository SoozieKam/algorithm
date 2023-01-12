# swea 2047 신문헤드라인
T = input()
print(T.upper())


# swea 2025 N줄덧셈
T = int(input())
sum = 0
for i in range(1, T+1):
    sum += i
print(sum)


# swea 1936 1대1 가위바위보
A, B = map(int, input().split())
if A == 3 and B == 1:
    print('B')
elif A == 1 and B == 3:
    print('A')
elif A > B:
    print('A')
else:
    print('B')


# swea 2027 대각선 출력하기
list = ['+', '+', '+', '+', '+']
for i in range(5):
    list[i] = '#'
    print("".join(list))
    list[i] = '+'


# swea 2058 자릿수 더하기
T = input()
result = 0
for i in range(len(T)):
    result += int(T[i])
print(result)


# swea 2019 더블더블
T = int(input())
for i in range(0, T):
    cnt = 2 ** i
    print(cnt, end=" ")
