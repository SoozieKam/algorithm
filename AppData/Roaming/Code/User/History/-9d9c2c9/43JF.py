T = int(input())
for t in range(1, T+1):
    N = int(input())
    my_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    my_list_2 = []
    for i in range(1, 10**6):
        num = str(i * N)
        for m in num:
            my_list_2.append(num[m:m+2])

        if list(set(sorted(my_list_2))) == my_list:
            break
            print(f'  # {t} {i})
