# 문제2
T = int(input())
for i in range(1, T+1):
    nums = list(map(int, input().split()))
    print(f'#{i} {int(sum(nums)/10)}')


# 문제3
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)


# 문제4
a = int(input())
for i in range(a):
    print('#', end="")

# 문제5
T = int(input())
for i in range(1, T+1):
    nums = list(map(int, input().split()))

    print(f'#{i} {max(nums)}')