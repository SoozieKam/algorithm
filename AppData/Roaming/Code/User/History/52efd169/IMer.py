# 문제1
num = int(input("'5'를 입력하세요."))
print(num)

# 문제2
nums = list(map(int, input("'2 5'를 입력하세요.").split()))
for i in nums:
    print(i, end=" ")

# 문제3
nums = list(map(int, input("'1 2 3'를 입력하세요.").split()))
for i in nums:
    print(i, end=" ")

# 문제4
strs = input("'word1 word2 word3'를 입력하세요.").split()
for i in strs:
    print(strs, end=" ")

# 문제5
nums = list(map(int, input("'1 2 3 4 5'를 입력하세요.").split()))
for i in nums:
    print(i, end=" ")

# 문제6
nums = list(map(int, input("'-10 10'를 입력하세요.").split()))
for i in nums:
    print(i, end=" ")

# 문제7
strs = input("'a b c d e'를 입력하세요.").split()
print(strs, end=" ")

# 문제8
nums = list(map(int, input("'3 17 1 39 8 41 2 32 99 2'를 입력하세요.").split()))
for i in nums:
    print(i, end=" ")

# 문제9
nums = list(map(int, input("'1 4 0 10 2 3 9'를 입력하세요")))
for i in nums:
    print(i, end=" ")
