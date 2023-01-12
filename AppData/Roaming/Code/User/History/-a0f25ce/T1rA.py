a = int(input())
my_list = []
for i in range(1, a+1):
    if a % i == 0:
        my_list.append(i)
        my_list.append(a//i)
set = sorted(set(my_list))
new_list = list(set)
print(new_list.join(), end=" ")
