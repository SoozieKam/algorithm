a = int(input())
my_list = []
for i in range(1, a+1):
    if a % i == 0:
        my_list.append(i)
        my_list.append(a//i)
new_list = list(sorted(set(my_list)))
for n in new_list:
    print(n, end=" ")
