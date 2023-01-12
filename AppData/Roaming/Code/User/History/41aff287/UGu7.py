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
