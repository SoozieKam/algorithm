N = int(input())
whos_enter = {}
for n in range(N):
    key, value = input().split()
    whos_enter[key] = value

for key in sorted(whos_enter.keys(), reverse=True):
    if whos_enter[key] == 'enter':
        print(key)