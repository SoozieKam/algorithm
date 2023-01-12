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
cnt = 1
my_dict = {}
for i in my_list:
    if i not in my_dict:
        my_dict[i] = cnt
    elif i in my_dict:
        cnt += 1
print(my_dict)


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

# ------------ 이제부터는 set 메서드 -----------
# set은 유일한 값의 모임
# 순서도 없고 반복 가능
# 주의할 건 set.pop()은 list.pop()과는 다르다는 거. 랜덤하게 반환. 왜? 인덱스가 없으니까.
# set.copy()
# set.add(x)
# set에서는 연산자 쓸 수 있음
# a-b : 차집합
# a\b : 합집합 등


# ------------ 이제부터 dictionary 메서드 -----
# 변경가능, 반복가능
# d.keys()
# d.values()
# d.items()
# d.pop() 딕셔너리는 중복된 key가 없으니까 이거 잘 사용할 수 있음.
# d.get(k) 키 k값을 반환, 근데 딕셔너리에 없으면 None반환
# 이건 d[k]랑 똑같음, 근데 딕셔너리에 없으면 key error 나옴

std = {"a": 20, "b": 22, "c": 30}
print(std.get("d", '찾을 수 없는 사람입니다.'))

# d.update(key = new value)ㄴ
# --> 이건 d[key]= new value 이거랑 똑같음 ...

# 정리
# 다 iterable !
# Sequence (순서 有)
# (1) string : 문자의 나열, mutable, iterable ""
# (2) list : mutable, iterable []
# (3) tuple : immutable(불변), iterable (0,1,3)
# (4) range : 숫자의 나열

# 컬렉션
# (1) set : mutable, iterable, 중복된 값 없음
# (2) dictionary : mutable, iterable, 중복된 값 없음
