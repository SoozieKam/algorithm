f = open('01.txt', 'w', encoding='UTF8')
f.write('hello python!\n')
for i in range(1, 6):
    f.write(f'{i}번째 파이썬 공부 중\n')

f.close()
