T = int(input())
for t in range(1, T+1):
    date = input()
    YYYY = date[:4]
    MM = date[4:6]
    DD = date[6:]

    if MM == '00' or DD == '00':
        print(-1)

    elif MM == '02':
        if int(DD) <= 28:
            print(f'#{t} {YYYY}/{MM}/{DD}')
        else:
            print(-1)

    elif int(MM) <= 12:
        if MM == '01' or MM == '03' or MM == '05' or MM == '07' or MM == '08' or MM == '10' or MM == '12':
            if int(DD) <= 31:
                print(f'#{t} {YYYY}/{MM}/{DD}')
            else:
                print(-1)
        elif int(DD) <= 30:
            print(f'#{t} {YYYY}/{MM}/{DD}')

        else:
            print(-1)
    else:
        print(-1)
