my_list = ['서울', '서울', '대전',
           '광주', '서울', '대전', '부산', '부산']

for i in my_list:
    if i in my_list:
        my_list.remove(i)

    elif i not in my_list:
        continue
print(len(my_list))
