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
str = '+++++'
for i in range(5):
    str(i) == '#'
    print(str)
