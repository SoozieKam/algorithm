# 문제1
cnt = -1
num_e = 0

my_list = input("문자열을 입력하세요").split()

for i in my_list:
    cnt += 1
    if i == 'e':
        num_e = cnt

if cnt == -1:
    num_e = -1

print(num_e)


# 문제2
cnt = 0
my_dict = {}

my_list = input("문자열을 입력하세요").split(" ")
for i in my_list:
    if i not in my_list:
        my_dict[i] = 1
    elif i in my_list:
        cnt += 1
        my_dict[i] = cnt
        cnt = 0

print(my_dict)
