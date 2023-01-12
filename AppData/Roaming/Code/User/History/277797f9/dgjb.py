T = int(input())
for t in range(1, T+1):
    date = input()
    YYYY = int(date[:5])
    MM = int(date[4:7])
    DD = int(date[7:])
    if MM == 02:
        if DD <= 28:
            print(f'#{t} {YYYY}/{MM}/{DD}')
        else:
            print(-1)
    elif MM <= 12:
        if MM == 01 or MM == 03 or MM == 05 or MM == 07 or MM == 08 or MM == 10 or MM == 12:
            if DD <= 31:
                print(f'#{t} {YYYY}/{MM}/{DD}')
            else:
                print(-1)
        else:
            if DD <= 30:
                print(f'#{t} {YYYY}/{MM}/{DD}')
            else:
                print(-1)
