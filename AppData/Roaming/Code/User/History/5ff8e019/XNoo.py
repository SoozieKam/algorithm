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
vowel = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
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

today = "20230105"
dict_variable["나이"] = int(today[:4]) - int(dict_variable["생년"][:4]) + 1

print("나이", ":", dict_variable["나이"])
