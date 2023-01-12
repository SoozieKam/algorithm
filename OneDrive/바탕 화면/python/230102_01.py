#문제1
number1 = int(input("정수형 숫자를 입력해주세요"))
print(number1)

#문제2
favorite_food = str(input("좋아하는 음식을 입력해주세요"))
print(favorite_food)

#문제3
your_name = str(input("이름을 입력해주세요"))
your_year = int(input("태어난 년도를 입력해주세요"))
your_age = 2023 - your_year + 1
print("저의 이름은", your_name, "이고, 올해 나이는", your_age, "입니다")

#문제4
first_st = str(input("첫 번째 문장을 입력해주세요"))
second_st = str(input("두 번째 문장을 입력해주세요"))
print(fisrt_st + second_st)

#문제5
number2 = int(input("정수형 숫자를 입력해주세요"))
number3 = number2 * -1
print(number3)

#문제6
number4 = int(input("첫 번째 정수형 숫자를 입력해주세요"))
number5 = int(input("두 번째 정수형 숫자를 입력해주세요"))
my_plus = number4 + number5
my_minus = number4 - number5
my_multiple = number4 * number5
my_div = number4/number5
my_namusi = number4 % number5
print(my_plus, my_minus, my_multiple, my_div, my_namusi)

#문제7
n1 = int(input("첫 번째 정수형 숫자를 입력해주세요"))
n2 = int(input("두 번째 정수형 숫자를 입력해주세요"))
n3 = int(input("세 번째 정수형 숫자를 입력해주세요"))
pg = (n1+n2+n3)/3
print(pg)

#문제8
n4 = int(input("첫 번째 정수형 숫자를 입력해주세요"))
n5 = int(input("두 번째 정수형 숫자를 입력해주세요"))
n6 = int(input("세 번째 정수형 숫자를 입력해주세요"))
n7 = int(input("네 번째 정수형 숫자를 입력해주세요"))
n8 = int(input("다섯 번째 정수형 숫자를 입력해주세요"))
print(list(n4, n5, n6, n7, n8))

#문제9
str_1 = str(input("문자열을 입력해주세요"))
int_1 = int(input("정수형 숫자를 입력해주세요"))
number_9 = str_1 * len(int_1)
print(number_9)

#문제10
n_1 = int(input("첫 번째 정수형 숫자를 입력해주세요"))
n_2 = int(input("두 번째 정수형 숫자를 입력해주세요"))
print(n_1 + n_2)
n_3 = int(input("세 번째 정수형 숫자를 입력해주세요"))
print(n_1 + n_2 + n_3)
n_4 = int(input("네 번째 정수형 숫자를 입력해주세요"))
print(n_1+ n_2 + n_3 + n_4)
n_5 = int(input("다섯 번째 정수형 숫자를 입력해주세요"))
print(n_1 + n_2 + n_3 + n_4 + n_5)
