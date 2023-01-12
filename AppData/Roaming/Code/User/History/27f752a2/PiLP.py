T = int(input())
cnt = 0
for t in range(1, T+1):
    N = list(map(int, input().split()))
    for i in N:
        if i % 2 == 1:
            cnt += i
    print(f'{t} {cnt}')
    cnt = 0
