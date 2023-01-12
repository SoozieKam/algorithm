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
# (1) print의 키워드(end) 써서 출력
for i in result:
    print(i, end="")

# (2) for로 반복하면서 문자열 만들기
text = ''
for elem in result:
    text += elem
print(text)

# (3) join 메서드
print('', join(result))

# cf 1 5 3 4로 띄어쓰기?
print(' ', join(result))

# ''''''''이까지는 문자열 얘기 '''
# 이제부터는 리스트

# L.append(x)
# L.extend(x) 리스트에 iterable 항목 추가
# L.insert(i, x)
# L.remove(x)
# L.pop(i) 그냥 pop하면 맨 뒤 값 삭제
# L.clear() 모든 항목 삭제
# L.index(x) x 값의 index 값 반환 (위치)
# --> 세 개 값 넣는 건 ?
# L.count(x) 값 개수 반환
# L.sort()하면 원본 자체가 변경
# sorted(L)하면 리스트를 정렬해서 보여줄 뿐 원본이 변경되지는 않음.
# L.reverse() 는 순서 뒤집음, 정렬하는 것이 아님! 걍 바뀜.
# --> 근데 걍 for 문 써도 됨
text = 'hello'
print(text[::-1])  # 이렇게 하면 뒤집힘.
