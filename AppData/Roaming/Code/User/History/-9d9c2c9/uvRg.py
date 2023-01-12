T = int(input())
for t in range(1, T+1):
    N = int(input())
    my_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    my_list_2 = []
    while True:
        i = 1
        num = str(i * N)
        for n in num:
            n = 0
            my_list_2.append(num[n])

            if my_list == list(set(sorted(my_list_2))):
                break

            else:
                i += 1
                n += 1

        print(f'#{t} {i}')
