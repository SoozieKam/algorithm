import json
f = open('fruits.txt', 'w', encoding='UTF8')
x = json.load(f)
cnt = len(x.split())
print(cnt)
f.write(str(cnt))
f.close()
