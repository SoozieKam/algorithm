# num = 2
# result == '홀' if num % 2 else result == '짝'

# List Comprehension
# 1~3의 세제곱의 결과가 담긴 리스트 만들기
list = []
for num in range(1, 4):
    list.append(num**3)
print(list)

# 이거를 한 줄로 나타내면 아래와 같음
[num**3 for num in range(1, 4)]

# Dictionary Comprehension
# 1~3의 세제곱 결과가 담긴 딕셔너리 만들기
dict = {}
for num in range(1, 4):
    dict[num] = num**3
print(dict)

# 한 줄로 나타내면
{num: num**3 for num in range(1, 4)}
