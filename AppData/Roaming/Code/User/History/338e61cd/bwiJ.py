num = int(input("정수 값을 넣으세요"))
if num % 2 ==0:
    print('짝수')
else: 
    print('홀수')

# 문제2
dust = int(input("미세먼지 농도는 무엇입니까?"))
if dust >=0 and dust < 30:
    print("좋음")

    elif dust >=30 and dust < 80 :
        print("보통")

        elif dust >=80 and dust <150 :
            print ("나쁨")

            else : 
                print ("매우나쁨")