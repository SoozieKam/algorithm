# while문 활용 (종료조건 필요)
n = 0
result = 0
num_1 = int(input("양의 정수를 입력하세요."))
while num_1 >= n:
    result += n
    n += 1
print(result)


# for문 활용 (반복 가능한 객체 n를 모두 순회하면 종료함. 종료조건 불필요)
target_number = 10
result = 0
for n in range(1, target_number+1):
    result += n
print(result)


# map 함수 : 리스트의 요소를 지정된 함수로 처리해주는 함수

# 만약 map 안 쓰고 실수 리스트의 모든 요소를 정수로 변환하려면?
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

# map 사용, 리스트 속 실수를 다 정수로 만들고 다시 리스트로 만들기
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

# 숫자 만들고 문자열로 변환
a = list(map(str, range(10))
print(a)
