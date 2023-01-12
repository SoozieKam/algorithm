f = open('fruits.txt', 'r', encoding='UTF8')
a = f.read()
cnt = map(list, a.split('\n'))
print(len(cnt))

f.close()
