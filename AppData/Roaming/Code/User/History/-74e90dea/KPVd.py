f = open('fruits.txt', 'r', encoding='UTF8')
a = f.read()
cnt = len((list(a.split('\n')))
print(cnt)

f.close()
