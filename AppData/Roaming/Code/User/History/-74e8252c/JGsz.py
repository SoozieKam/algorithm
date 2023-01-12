from collections import Counter

f = open('fruits.txt', 'r', encoding='UTF8')
w = open('04.txt', 'w', encoding='UTF8')

a = f.read()
fruits_count = Counter(a)
print(fruits_count)
