a = int(input())
list = []
for i in range(1, a+1):
    if a % i == 0:
        list.append(i)
        list.append(a//i)
set = sorted(set(list))
new_list = list(set)
print(new_list.join(), end=" ")
