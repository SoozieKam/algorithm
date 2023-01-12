# 문제1
e_cnt = 0
cnt = map(str, input("문자열을 입력하세요").split)
for i in cnt:
    if i == "e":
        e_cnt += 1
    else:
        continue
print(e_cnt)
