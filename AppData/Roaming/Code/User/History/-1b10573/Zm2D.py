my_list = ['서울', '서울', '대전',
           '광주', '서울', '대전', '부산', '부산']

for i in my_list:
    if i in my_list:
        my_list.remove(i)

    elif i not in my_list:
        continue
print(len(my_list))


# 다른 풀이
result = []
for i in my_list:
    if i not in result:
        result.append(i)
print(len(result))

# set을 쓰면 순서가 바뀜, 그래서 순서 중요한 경우에는 set 쓰지 말기
# 만약 지역별 갯수를 구하라 하면 dict 쓰는 게 낫겠지

# s.replce(old, new, count)
# '\n'.strip()
# .split()

a, b = map(int, input().split())
print(a + b)

# 문자열 변경
result = ['1', '5', '3']

# 결과가 153으로 출력되도록 하고 싶다면?
print(result, sep="")
