
f = open('fruits.txt', 'r', encoding='UTF8')
w = open('04.txt', 'w', encoding='UTF8')

a = f.read()
b = []

k = a.split('\n')
set_f = set(k)
list_f = list((set_f))
cnt = 0

for i in range(len(list_f)):
    for j in range(len(k)):
        if list_f[i] == k[j]:
            cnt += 1
        else:
            pass
    b.append([list_f[i], cnt])
    cnt = 0

print(b)
w.write(str(cnt))
f.close()
