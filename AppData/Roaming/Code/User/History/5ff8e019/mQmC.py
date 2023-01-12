# 문제1
import datetime
cnt = 0
my_str = str(input("문자열을 입력하세요"))
for i in my_str:
    if i == "e":
        cnt += 1
    else:
        continue
print(cnt)


# 문제2
cnt = 0
vowel = ["a", "A", "e", "E", "i, "I", "o", "O", "u", "U"]
my_str = str(input("문자열을 입력하세요"))
for i in my_str:
    if i in vowel:
        cnt += 1
    else:
        continue
print(cnt)


# 문제3
# datetime 을 정수로 바꿀 순 없으려나 ...
dict_variable = {
    "이름": "정우영",
    "생년": "20000101",
    "회사": "하이퍼그로스",
}

today = datetime.date(2023, 1, 5)
birthday = datetime.date(
    dict_variable[0:5], dict_variable[5:7], dict_variable[7:])

age = today - birthday
dict_variable["나이"] = age

print("나이", dict_variable["나이"])
