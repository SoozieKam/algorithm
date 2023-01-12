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


numbers = ['1', '2', '3']
# [1, 2, 3]으로 바꾸고 싶다면?
# int: 함수
new_numbers = list(map(int, numbers))

numbers = [[2, 1], [1, 3]]
# [[1,2], [1,3]]
# sorted : 함수
print(list(map(sorted, numbers)))

# cf) 이렇게 쓰면 안됨
# print(list(map(numbers.sort, numbers)))


numbers = [2, 4]
# 2로 나눈 몫으로만 구성된
# [1, 2]
# 함수를 만들면 됨.


def a(n):
    return n//2


print(list(map(a, numbers)))

# 만약 여기서 한번만 쓰는 함수라고 하면 lambda 쓰면 됨
print(list(map(lambda n: n//2, numbers)))

# 이렇게 쓸 수도
print([n//2 for n in numbers])

# 기본은 이렇게
new_numbers = []
for n in numbers:
    new_numbers.append(n//2)
print(new_numbers)

# 메서드는 함수 자리에 못 씀 함수 객체만 들어갈 수 있음
