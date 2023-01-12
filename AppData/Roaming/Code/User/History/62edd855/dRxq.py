import datetime
import random
phone_book = {
    '전화번호': '114',
    '피자헛': '15885588',
    '김탁희': '01052216086',
    '대리운전': '15717777'
}

# name 은 변수의 이름
for name in phone_book:
    # 키 순회
    print(phone_book)

    # 값 순회
    print(phone_book[name])


# import 모듈을 가져오는 것

# random.sample(population, k)
# Return a k length list 6개 숫자
# the population sequence, 1~45개 숫자 중
numbers = range(1, 46)
lotto = random.sample(numbers, 6)
print(sorted(lotto))
# range도 sequence여서 list로 바꿀 필요가 없음.


# .sort()와 sorted()의 차이
numbers = [10, 2, 5]
print(numbers.sort())  # None
print(sorted(numbers))  # [2, 5, 10]

# .sort(): 메서드
# return : None
# 해당 리스트 자체를 정렬해줌.
numbers = [10, 2, 5]
numbers.sort()
print(numbers)  # 이렇게 하면 None 대신 제대로 나옴

# sorted(): 함수


# 발표 순서 정하기
students = ['a', 'b', 'c', 'd']
random.shuffle(students)
print(students)


# datetime
print(datetime.datetime.now())
today = datetime.date(2023, 1, 5)
end = datetime.date(2023, 6, 14)
print(f'우리가 개발자가 되는 데 걸리는 시간 ...{end- today}')
