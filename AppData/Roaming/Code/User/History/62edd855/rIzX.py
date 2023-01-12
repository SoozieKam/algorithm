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
menu = ['초밥', '국밥', '햄버거']
print(random.choice[menu])

# random.sample(population, k)
# Return a k length list 6개 숫자
# the population sequence, 1~45개 숫자 중
numbers = range(1, 46)
print(random.sample(numbers, 6))

# range도 sequence여서 list로 바꿀 필요가 없음.
