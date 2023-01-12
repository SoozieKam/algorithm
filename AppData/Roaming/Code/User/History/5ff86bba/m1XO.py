# 예제1
dict_variable = {}
dict_variable["이름"] = "정우영"
dict_variable["생년월일"] = "19000101"
dict_variable["회사"] = "하이퍼그로스"

print(dict_variable["이름"])  # 정우영
print(dict_variable["생년월일"])  # 19000101
print(dict_variable["회사"])  # 하이퍼그로스


# 예제2
dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"

print(dict_variable["a"])  # A
print(dict_variable["D"])  # d
print(dict_variable["b"])  # 에러 남


# 예제3
dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"] + dict_variable["banana"])  # 9000


# 예제4
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key in dict_variable:
    print(key, dict_variable[key])

"""
이름, 정우영 
생년월일, 19000101
회사, 하이퍼그로스 
"""


# 예제5
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key, value in dict_variable.items():
    print(key, value)

"""


"""


# 예제6
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

print("나이" in dict_variable)  # ?


# 예제7
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # 위 조건문의 조건식이 무엇을 의미하는지 작성하세요.
    # ?

print(dict_variable)  # ?


# 예제8
list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])

except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
출력 결과를 예측해서 작성하세요.
?
"""


# 예제9
try:
    number = 1
    if number == 1
    print(number)


except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
에러 원인

"""


# 예제10
n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3

print(total)  # ?