# 문제1
import sys
sys.stdin = open(r"C:\Users\rkatn\OneDrive\바탕 화면\python\input.txt", "r")

nums = map(int, input().split())
for i in nums:
    print(i, end=" ")


# 문제2
str = input().split()
for i in str:
    print(i, end=" ")


# 문제3
T = int(input())
print(T)
for t in range(1, T+1):
    N = int(input())
    print(N)
    for _ in range(N):
        num = int(input())
        print(num)


# 문제4
T = int(input())
print(T)
for t in range(1, T+1):
    N = int(input())
    print(N)
    for _ in range(N):
        a, b = map(int, input().split())
        print(a, b)


# 문제5
T = int(input())
print(T)
for t in range(1, T+1):
    N = int(input())
    print(N)
    for _ in range(N):
        S = input().split()
        for i in S:
            print(i, end=" ")


# 문제6
T = int(input())
print(T)
for t in range(1, T+1):
    N = int(input())
    print(N)
    for _ in range(N):
        nums = list(map(int, input().split()))
        for i in nums:
            print(i, end=" ")


# 문제7
T, N = map(int, input().split())
print(T, N)
for t in range(1, T+1):
    for _ in range(N):
        nums = map(int, input().split())
        for i in nums:
            print(i, end=" ")


# 문제8
T, N = map(int, input().split())
print(T, N)
for t in range(1, T+1):
    for _ in range(N):
        a, b = map(int, input().split())
        print(a, b)


# 문제9
T, N = map(int, input().split())
print(T, N)
for t in range(1, T+1):
    for _ in range(N):
        nums = map(int, input().split())
        for i in nums:
            print(i, end=" ")
