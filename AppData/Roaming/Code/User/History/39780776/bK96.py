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

# 다른 풀이


class player:
    def __init__(self, name, wep):
        self.name = name
        self.wep = wep

    def __gt__(self, other):
        if self.wep % 3 == (other.wep+1) % 3:
            return self
        else:
            return other

    def __str__(self):
        return self.name


a, b = map(int, input().split())
p1 = player('A', a)
p2 = player('B', b)
print(p1 > p2)

# swea 2027 대각선 출력하기
list = ['+', '+', '+', '+', '+']
for i in range(5):
    list[i] = '#'
    print("".join(list))
    list[i] = '+'


# swea 2058 자릿수 더하기
T = input()
result = 0
for i in T:
    result += int(T[i])
print(result)


# swea 2019 더블더블
T = int(input())
for i in range(T+1):
    cnt = 2 ** i
    print(cnt, end=" ")
