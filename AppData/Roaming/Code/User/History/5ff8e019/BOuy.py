# 문제1

cnt = 0
my_str = str(input("문자열을 입력하세요"))
for i in my_str:
    if i == "e":
        cnt += 1

print(cnt)


# 문제2
cnt = 0
vowel = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
my_str = str(input("문자열을 입력하세요"))
for i in my_str:
    if i in vowel:
        cnt += 1

print(cnt)


# 문제3
dict_variable = {
    "이름": "정우영",
    "생년": "20000101",
    "회사": "하이퍼그로스",
}

today = "20230105"
dict_variable["나이"] = int(today[:4]) - int(dict_variable["생년"][:4]) + 1

print("나이", ":", dict_variable["나이"])


# 문제4
name = input("이름을 입력하세요")
phone_num = input("전화번호를 입력하세요")
address = input("거주지를 입력하세요")

dict_aboutme = {
    "이름": name,
    "전화번호": phone_num,
    "거주지": address.address,
}
print(dict_aboutme)
for key, value in dict_aboutme.items():
    print(f"{key}:{value}")

# 문제5
name = input("이름을 입력하세요")
phone_num = input("전화번호를 입력하세요")
email = input("이메일을 입력하세요")
address = input("거주지를 입력하세요")

dict_1 = {
    name: {
        "전화번호": phone_num,
        "이메일": email,
        "거주지": address
    }
}
print(dict_1)


# 문제6
cnt = 1
dict_my = {}
my_str = str(input("문자열을 입력하세요"))
my_set = set(my_str)
for i in my_str:
    for j in my_set:
        if i == j:
            dict_my[i] = 1


print(dict_my)
