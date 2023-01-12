# 문제1
n_1 = int(input("정수를 입력하세요"))
if n_1 >= 0:
    print(n_1)
else:
    print(n_1 * -1)


# 문제2
result = 0
number_list = [1, 2, 3, 4, 5]
for i in number_list:
    result += 1
print(result)


# 문제3
result = 0
number_list = [1, 2, 3, 4, 5]
for i in number_list:
    result += i
print(result)


# 문제4
len_1 = 0
sum_1 = 0
number_list = [2, 4, 6]
for i in number_list:
    len_1 += 1
    sum_1 += i
print(sum_1 / len_1)


# 문제5
number_list = [1, 2, 3, 4, 5]
for i in number_list:
    i *= i
print(i)
