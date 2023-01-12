# chapter02_2
# 파이썬 완전 기초
# 파이썬 변수

# 파이썬 변수
n = 700
print(n)

# 출력
print(type(n))
# 700은 정수형이야 라고 알려주는 것

# 동시 선언
x = y = z = 700
print(x, y, z)

# 선언
var = 75

# 재선언
var = 'Change Value'

# 출력
print(type(var))
# var의 type은 string이야. 문자열이야.

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 생성

# 예1
print(300)
print(int(300))

# 예2
# n -> 777
n = 777

print(n, type(n))
print(n)

m = n
# m -> 777 <- n

print(m, n)

m = 400

print(m, n)

# id(identity 확인; 객체의 고유값 확인)

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Methond 선언 시 사용
# Pascal Case : NumberOfCollegeGraduates -> Class 선언 시 사용
# Snake Case : number_of_college_graduates -> 변수 선언 시 사용
# 파스칼 케이스를 변수에 사용하는 건 매우 좋지 않음

age = 1
Age = 2
aGe = 3
a_g_e = 4
_age = 5
age_ = 7
_AGE_ = 7

# 예약어는 변수명으로 불가능
# as , class 등은 에러가 남. 예약어여서
# python reserved words 검색해서 나오는 것들은 안됨 예제에 있음
