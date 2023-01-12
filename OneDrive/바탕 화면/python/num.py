num = int(input("정수 값을 넣으세요"))
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 문제2
dust = int(input("미세먼지 농도는 무엇입니까?"))
if dust > 150:
    print("매우나쁨")

    elif dust > 80:
        print("나쁨")

        elif dust > 30:
            print("보통")

            else:
                print("좋음")
