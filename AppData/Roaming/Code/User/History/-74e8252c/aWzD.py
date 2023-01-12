
f = open('fruits.txt', 'r', encoding='UTF8')
w = open('04.txt', 'w', encoding='UTF8')

a = f.read()
b = []

set_f = (set((a.split('\n'))))
list_f = (list(set((a.split('\n')))))
cnt = 0 

for i in range(len(list_f)):
    for j in range(len(set_f)):
        if list_f[i] == set_f[j]:
            cnt += 1
        else: 
            pass
    b.append([list_f[i], cnt])
    
print(num)
w.write(str(cnt))
f.close()