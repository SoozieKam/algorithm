# 문제1
cnt = 0
num_e = 0

my_list = input("문자열을 입력하세요").split()

for i in my_list:
    cnt += 1
    if i == 'e':
        num_e += cnt-1

if cnt = 0:
    num_e = -1

print(num_e)
