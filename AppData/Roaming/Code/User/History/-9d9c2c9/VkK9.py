T = int(input())
for t in range(1, T+1):
    N = int(input())
    my_list = []
    for i in range(1, 10**6):
        i = 1
        num = str(i * N)
        for n in num:
            my_list.append(num[n])

            if list(set(sorted(my_list))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                break

        print(f'#{t} {i}')
