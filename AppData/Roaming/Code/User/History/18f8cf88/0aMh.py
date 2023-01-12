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
