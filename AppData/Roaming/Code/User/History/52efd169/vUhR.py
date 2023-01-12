my_list = [1, 2, 3, 4, 5, 6, 1, 2]
cnt = 1
my_dict = {}
for i in my_list:
    if i not in my_dict:
        my_dict[i] = cnt
    elif i in my_dict:
        cnt += 1
print(my_dict)
