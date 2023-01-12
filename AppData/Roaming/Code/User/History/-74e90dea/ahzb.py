f = open('fruits.txt', 'r', encoding='UTF8')
a = f.read()
cnt = len(a.split())
print(cnt)

f.close()
