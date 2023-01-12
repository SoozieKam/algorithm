f = open('fruits.txt', 'w', encoding='UTF8')
cnt = len('fruits.txt'.split('\n'))
f.write(str(cnt))
f.close()
