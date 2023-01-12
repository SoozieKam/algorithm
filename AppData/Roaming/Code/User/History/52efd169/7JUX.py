my_list = [1, 2, 3, 4, 5, 6, 1, 2]
my_dict = {}
for i in my_list:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print(my_dict)

# 아래 코드도 가능하긴 한데 좀 비효율적이라고 함
