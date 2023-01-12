# 문제1
cnt = -1
num_e = 0

my_list = input("문자열을 입력하세요").split()

for i in my_list:
    cnt += 1
    if i == 'e':
        num_e = cnt
    else:
        continue

if num_e == 0:
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
