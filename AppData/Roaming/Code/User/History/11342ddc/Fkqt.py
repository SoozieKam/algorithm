# 문제1
cnt = -1
num_e = 0

my_list = input("문자열을 입력하세요").split()
print(my_list)

for i in my_list:
    cnt += 1
    if i == 'e':
        num_e = cnt
        break
    else:
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


# 문제 5 답
n = int(input())
result = 0

while n > 0:
    n //= 10
    result += n % 10

print(result)

# 위에 것처럼 하면 하나씩 밀림, 자리 바꿔줘야 함
n = int(input())
result = 0

while n > 0:
    result += n % 10
    n //= 10

print(result)

# 문자열 str() 함수 사용하면?

# 하나의 숫자를 입력 받아서 세제곱 반환하는 함수 cube


# 문제1 답
string = input("문자열을 입력하세요 > ")
for index in range(len(string)):
    if string[index] == 'e':
        print(index)
        break
else:
    print(-1)

# 문제1 방법 2
string = input("문자열을 입력하세요 > ")
result = -1
for index in range(len(string)):
    if string[index] == 'e':
        result = index
print(result)

# 문제2 답
string = input("문자열을 입력하세요 > ").split()
dict_var = {}

for word in string:
    if word in dict_var:
        dict_var[word] += 1

    elif word not in dict_var:
        dict_var[word] = 1

for key, value in dict_var.items():
    print(f"{key} {value}")


# 문제3 답
string = input("문자열을 입력하세요 > ")
new_string = ""
for char in string:
    if char != 'e':
        new_string += char
print(new_string)


# 문제4 답
string, alpha = input("문자열을 입력하세요 > ").split()
count = 0
for char in string:
    if char == alpha:
        count += 1

print(count)


# 문제5 답
string_list = input("문자열을 입력하세요 > ").split()

# 방법 1
print(string_list[0], string_list[1], string_list[2], sep='-')

# 방법 2
print(*string_list, sep="-")


# 문제6 답
number = int(input("양의 정수를 입력하세요 > "))
if number < 0:
    print(-1)

else:
    total = 0
    while number > 0:
        n = number % 10
        total = total + n
        number = number // 10
    print(total)
