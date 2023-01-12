# 문제1
# e_cnt = 0
# cnt = list(map(str, input("문자열을 입력하세요").split))
# for i in len(cnt):
#    if i == "e":
#        e_cnt += 1
#    else:
#        continue
# print(e_cnt)

cnt = 0
my_str = str(input("문자열을 입력하세요"))
for i in my_str:
    if i == "e":
        cnt += 1
    else:
        continue
print(cnt)
