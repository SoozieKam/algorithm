a = int(input())
list = []
for i in range(1, a+1):
    if a % i == 0:
        list.append(i)
        list.append(a//i)
new_list = set(list.sort())
print(new_list)