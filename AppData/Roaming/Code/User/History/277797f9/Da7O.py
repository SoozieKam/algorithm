T = int(input())
for t in range(1, T+1):
    date = input()
    YYYY = int(date[:4])
    MM = int(date[4:7])
    DD = int(date[7:])

    print(f'#{t} {YYYY}/{MM}/{DD}')

    if MM == 2:
        if DD <= 28:
            print(f'#{t} {YYYY}/{MM}/{DD}')
        else:
            print(-1)
    elif MM <= 12 and MM > 0:
        if MM == 1 or MM == 3 or MM == 5 or MM == 7 or MM == 8 or MM == 10 or MM == 12:
            if DD <= 31:
                print(f'#{t} {YYYY}/{MM}/{DD}')
            else:
                print(-1)
        else:
            if DD <= 30:
                print(f'#{t} {YYYY}/{MM}/{DD}')
            else:
                print(-1)
