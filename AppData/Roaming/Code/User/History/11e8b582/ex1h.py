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
result = 1
number_list = [1, 2, 3, 4, 5]
for i in number_list:
    result *= i
print(result)


# 문제6
number_list = [1, 2, 3, 4, 5]
number_list.sort()
print(number_list.pop())


# 문제6 for문으로 풀기
number_list = [1, 2, 3, 4, 5]

# max_value = 리스트의 첫 번째 값
max_value = number_list[0]

# number_list 반복, number!
for number in number_list:

    # 만약 max_value보다 number가 크면
    if max_value <= number:

        # 값 교체
        max_value = number
print(max_value)


# 문제7
number_list = [1, 2, 3, 4, 5]
number_list.sort()
print(number_list.pop(0))
