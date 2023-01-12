T = int(input())
for t in range(1, T+1):
    date = input()
    YYYY = date[:4]
    MM = date[4:6]
    DD = date[6:]

    print(f'#{t} {YYYY}/{MM}/{DD}')

    if YYYY == '0000' or MM == '00' or DD == '00':
        print(-1)

    elif MM == '02':
        if int(DD) <= 28:
            print(f'#{t} {YYYY}/{MM}/{DD}')
        else:
            print(-1)
    elif int(MM) <= 12:
        if int(MM) == 1 or int(MM) == 3 or int(MM) == 5 or int(MM) == 7 or int(MM) == 8 or int(MM) == 10 or int(MM) == 12:
            if int(DD) <= 31:
                print(f'#{t} {YYYY}/{MM}/{DD}')
            else:
                print(-1)
        else:
            if int(DD) <= 30:
                print(f'#{t} {YYYY}/{MM}/{DD}')
            else:
                print(-1)
    else:
        print(-1)
