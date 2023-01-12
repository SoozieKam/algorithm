with open('01.txt', 'r', encoding='UTF8') as f:
    read_data = f.read()
print("hello python!")
for i in range(1, 6):
    print(f'{i}일차 파이썬 공부 중')
f.closed
