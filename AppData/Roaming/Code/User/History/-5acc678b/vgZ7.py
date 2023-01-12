T = int(input())
k = 0
for i in range(1, T+1):
    nums = list(map(int, input().split()))
    for n in nums:
        n += n
    k += 1
    print(f'#{k} {int(n/10)}')
