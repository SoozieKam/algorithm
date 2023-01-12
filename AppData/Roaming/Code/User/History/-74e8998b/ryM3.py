f = open('fruits.txt', 'r', encoding='UTF8')
w = open('03.txt', 'w', encoding='UTF8')

cnt = 0
a = f.read()

i = (list(a.split('\n')))
for b in i:
    if "berry" in b:
        cnt += 1
w.write(str(cnt))
f.close()
