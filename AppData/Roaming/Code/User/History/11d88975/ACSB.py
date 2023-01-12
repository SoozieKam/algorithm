# 문제1
n_1 = int(input("정수를 입력하세요."))
if n_1 > 0:
    print("True")
else:
    print("False")


# 문제2
n_2 = int(input("첫 번째 정수를 입력하세요."))
n_3 = int(input("두 번째 정수를 입력하세요."))
if n_2 > n_3:
    print(n_2)
elif n_2 == n_3:
    print("False")
else:
    print(n_3)


# 문제3
n_4 = int(input("정수를 입력하세요."))
if n_4 >= 10 or n_4 <= 1:
    print("False")
else:
    print("True")


# 문제4
n_5 = int(input("정수를 입력하세요."))
if n_5 > 0 and n_5 % 2 == 0:
    print("True")
else:
    print("False")


# 문제5
n_6 = int(input("정수를 입력하세요."))
if n_6 > 100 or n_6 < 0:
    print("에러")
elif n_6 >= 60:
    print("합격")
else:
    print("불합격")


# 문제6
s_1 = str(input("문자열을 입력하세요."))
for i in s_1[::-1]:
    print(i)


# 문제7
n_7 = int(input("정수를 입력하세요."))
n_8 = int(input("정수를 입력하세요."))
if n_7 == n_8:
    print("False")
elif n_7 > n_8:
    for i in range(n_7: n_8: 1)
    print(i)
else:
    for i in range(n_8: n_7: 1)
    print(i)
